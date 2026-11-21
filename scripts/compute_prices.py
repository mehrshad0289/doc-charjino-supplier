#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
compute_prices.py — محاسبه قیمت خرید نهایی تأمین‌کنندگان بین‌المللی و مقایسه با میانگین بازار ایران
منبع داده: IRAN-MARKET-PRICING.md (ادغام S01+S02)، مشاهده‌های مستقیم 2026-11-21.
خروجی: چاپ جدول‌ها + ذخیره JSON برای ژنراتور Word.
"""
import json, os

# ---------- FX ----------
USDT_TOMAN = 272300          # Wallex API 272264 (2026-11-21 ~21:40) گردش به بالا — [تأییدشده با منبع]
HKD_USD = 1 / 7.844282       # open.er-api.com 2026-11-20 — [تأییدشده با منبع]
TRY_USD = 1 / 50.534266
EUR_USD = 1 / 0.910749
RUB_USD = 1 / 82.021771
CONV_SPREAD = 0.01           # اسپرد خرید USDT ~1% — [تخمین]
TRC20_FEE_USDT = 1.0         # کارمزد شبکه per invoice — [تخمین]
BATCH_N = 50                 # سناریوی خرید دسته‌ای (مهم: تک‌سفارش غیراقتصادی است)

def toman(usd: float) -> float:
    """دلار → تومان با اسپرد خرید"""
    return usd * USDT_TOMAN * (1 + CONV_SPREAD)

def fmt(x: float) -> str:
    return f"{x:,.0f}"

# ---------- ایران: قیمت‌های مشاهده‌شده ----------
iran = {
    "PSN_US_10":  {"prices": [3348000, 2992000, 3328000], "sellers": ["Digi720", "GiftcardStore", "Gamalop(اسنیپت)"], "label": "S01"},
    "PSN_US_25":  {"prices": [7550000, 7081470, 6641000], "sellers": ["Digi720", "GiftcardStore", "RpStore(اسنیپت)"], "label": "S01"},
    "PSN_US_50":  {"prices": [13000000, 13620600, 9672000], "sellers": ["کاسپین گیفت", "YungCenter", "NICGift(پرچم‌دار)"], "label": "S02"},
    "XBOX_US_10": {"prices": [2859000, 2520000, 2595000], "sellers": ["GiftcardStore", "Emalls(9 فروشنده)", "Viramoj(اسنیپت)"], "label": "S01"},
    "ESHOP_US_10": {"prices": [2599000, 2601000, 2555700], "sellers": ["Giftro(اسنیپت)", "Aria Gift/Emalls", "Torob(اسنیپت)"], "label": "S01"},
    "ESHOP_US_50": {"prices": [12632500, 12100000, 11213000], "sellers": ["Torob پرترافیک", "وب گیفت", "گیفت پرشیا"], "label": "S02"},
    "PSPLUS_ES_12M_US": {"prices": [21587500, 22236000, 20700000], "sellers": ["Cardtak", "CDKeY", "Pspro(اسنیپت)"], "label": "S01"},
    "GPU_1M_OFFICIAL": {"prices": [2939000, 3969000, 3465000], "sellers": ["آگریگیتور(اسنیپت)", "فروشگاه(اسنیپت)", "Gametano(اسنیپت)"], "label": "S01"},
}
iran_avg = {k: sum(v["prices"]) / len(v["prices"]) for k, v in iran.items()}

print("=" * 88)
print("میانگین بازار ایران (تومان) — نرخ USDT مرجع:", f"{USDT_TOMAN:,}")
print("=" * 88)
for k, v in iran_avg.items():
    per_usd = v / (int(k.split("_")[-1]) if k.split("_")[-1].isdigit() else 1)
    print(f"{k:22s} avg={fmt(v):>14}  per-unit={fmt(per_usd)}  ({iran[k]['label']})")

# ---------- تأمین‌کنندگان: مدل هزینه ----------
results = {}

# --- Bitrefill: قیمت نقدی تأییدشده PSN US ($25–$250)؛ فاکتور با USDT؛ کارمزد شبکه per invoice
# سناریو: خرید دسته‌ای N کارت با یک فاکتور → کارمزد شبکه تقسیم بر N
br = {}
for sku, face in [("PSN_US_25", 25), ("PSN_US_50", 50), ("ESHOP_US_50", 50)]:
    usd_cost = face + TRC20_FEE_USDT / BATCH_N          # بدون تخفیف
    cost = toman(usd_cost)
    diff = (cost - iran_avg[sku]) / iran_avg[sku] * 100
    br[sku] = {"face_usd": face, "usd_cost": round(usd_cost, 3), "toman_cost": cost, "diff_pct": round(diff, 1)}
    results.setdefault("bitrefill", {})[sku] = br[sku]

# --- Cryptorefills: تسویه per-order با USDT-Tron؛ قیمت PSN طبق صفحه فروشگاه (فرض face — نیازمند تأیید US storefront)
for sku, face in [("PSN_US_25", 25)]:
    usd_cost = face + TRC20_FEE_USDT / BATCH_N
    cost = toman(usd_cost)
    diff = (cost - iran_avg[sku]) / iran_avg[sku] * 100
    results.setdefault("cryptorefills", {})[sku] = {
        "face_usd": face, "usd_cost": round(usd_cost, 3), "toman_cost": cost,
        "diff_pct": round(diff, 1), "note": "قیمت storefront مشاهده شد؛ نرخ دقیق US storefront نیازمند تأیید"}

# --- CoinGate GIFQ: تخفیف کاتالوگ PlayStation «up to -13%»؛ USDT تأییدنشده → دو سناریو
cg = {}
for sku, face in [("PSN_US_25", 25)]:
    for disc, tag in [(0.13, "best(-13%)"), (0.0, "worst(0%)")]:
        usd_cost = face * (1 - disc) + TRC20_FEE_USDT / BATCH_N
        cost = toman(usd_cost)
        diff = (cost - iran_avg[sku]) / iran_avg[sku] * 100
        cg[f"{sku}_{tag}"] = {"face_usd": face, "discount": disc, "usd_cost": round(usd_cost, 3),
                              "toman_cost": cost, "diff_pct": round(diff, 1)}
results["coingate_gifq"] = cg

# --- Kinguin: PSN US $10 = HK$80.39 (مشاهده 2026-11-21، 15 پیشنهاد) → USD
king = {}
hkd_price = 80.39
usd_price = hkd_price * HKD_USD          # ~10.25
cost = toman(usd_price)
diff = (cost - iran_avg["PSN_US_10"]) / iran_avg["PSN_US_10"] * 100
king["PSN_US_10"] = {"hkd_price": hkd_price, "usd_price": round(usd_price, 2), "toman_cost": cost,
                     "diff_pct": round(diff, 1), "note": "قیمت خرده مارکت‌پلیس؛ Wholesale tier پشت لاگین؛ پرداخت رمزارزی مستقیم ندارد"}
results["kinguin"] = king

# --- Gamivo: GPU 12M EU = €125.44–132.69 (اسنیپت) → USD → تومان؛ مقایسه ایران نداریم
gam = {}
mid_eur = (125.44 + 132.69) / 2
usd = mid_eur * EUR_USD
gam["GPU_12M_EU"] = {"eur_mid": mid_eur, "usd_mid": round(usd, 2), "toman_cost": toman(usd),
                     "note": "SKU مشابه 12M EU در ایران جمع‌آوری نشده → مقایسه ممکن نیست"}
results["gamivo"] = gam

# --- MTCGAME: قیمت عمومی ندارد → CONTACT REQUIRED
results["mtcgame"] = {"status": "CONTACT REQUIRED",
                      "note": "Authorized Reseller سونی؛ قیمت عمده فقط با استعلام مستقیم"}

# --- PS Plus 12M TR از منبع ترکیه (اسنپ‌شات S02: ~5,560 TRY — نیازمند استعلام)
try_price = 5560 * TRY_USD
results["tr_psplus"] = {"try_price": 5560, "usd_price": round(try_price, 2), "toman_cost": toman(try_price),
                        "diff_vs_iran_single": round((toman(try_price) - 35896000) / 35896000 * 100, 1),
                        "note": "منبع TRY نیازمند استعلام؛ ایران فقط 1 فروشنده"}

print("\n" + "=" * 88)
print("هزینه نهایی تأمین‌کننده در برابر میانگین ایران (منفی = ارزان‌تر)")
print("=" * 88)
for sup, skus in results.items():
    if sup in ("mtcgame",):
        print(f"\n{sup}: {skus['status']} — {skus['note']}")
        continue
    print(f"\n{sup}:")
    for sku, d in skus.items():
        if not isinstance(d, dict):
            continue
        base = iran_avg.get(sku.split("_best")[0].split("_worst")[0])
        line = f"  {sku:22s} cost={fmt(d.get('toman_cost', 0)):>14} toman"
        if base and "diff_pct" in d:
            line += f"   diff={d['diff_pct']:+.1f}%"
        print(line + (f"   [{d.get('note','')[:60]}]" if d.get("note") else ""))

# ---------- ذخیره JSON ----------
out = {"fx": {"usdt_toman": USDT_TOMAN, "hkd_usd": round(HKD_USD, 6), "try_usd": round(TRY_USD, 6),
              "eur_usd": round(EUR_USD, 6), "rub_usd": round(RUB_USD, 6), "conv_spread": CONV_SPREAD,
              "trc20_fee_usdt": TRC20_FEE_USDT, "batch_n": BATCH_N},
       "iran_avg": {k: round(v) for k, v in iran_avg.items()},
       "iran_detail": {k: {"prices": v["prices"], "sellers": v["sellers"]} for k, v in iran.items()},
       "suppliers": results}
dest = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(dest, exist_ok=True)
with open(os.path.join(dest, "computed_prices.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f"\nJSON saved → {dest}/computed_prices.json")
