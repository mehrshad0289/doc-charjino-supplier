# GAMES-COVERAGE — کدام تأمین‌کننده برای «بازی‌ها» به شارژینو خدمات می‌دهد؟ (2026-11-21)

> پرسش کارفرما: «مواردی که برای بازی‌ها می‌تواند ما را پشتیبانی کند کدام‌اند؟» این فایل، نیازهای محصول بازی شارژینو را به تأمین‌کنندگان بررسی‌شده نگاشت می‌کند. همه برچسب‌ها طبق قانون پروژه. Pull از GitHub انجام شد و مخزن Sync بود (HEAD = eba1ef4).

## نکته ساختاری مهم قبل از جدول

برای کنسول‌ها، «تأمین بازی» در بازار قانونی جهانی از سه مکانیزم می‌آید — نه از یک کاتالوگ کلید PS5 عمده‌فروشانه کلاسیک:

1. **کیف پول استور (گیفت‌کارت PSN/Xbox/eShop)** — مشتری خودش هر بازی را از استور ریجن می‌خرد؛ این رایج‌ترین و تمیزترین مسیر بومی‌سازی بازی در فروشگاه‌های ایرانی است.
2. **کانال رسمی توزیع‌کننده** — کدهای PSN از کانال رسمی Sony (نمونه: MTCGAME) و کدهای Xbox.
3. **کلید/کد از مارکت‌پلیس‌ها** — Kinguin، Gamivo، CodesWholesale (منشأ per-seller متغیر؛ برای کنسول بیشتر «کد استور/اشتراک» است تا کلید مستقل).

دسته چهارم (اکانت ظرفیتی/Primary-Secondary) کانال قانونی بین‌المللی ندارد — نقض ToS سونی مستند در SUPPLIER-INDEX.md. [ردشده]

## جدول نگاشت: نیاز بازی شارژینو → تأمین‌کننده

| نیاز محصولی | مکانیزم | تأمین‌کنندگان (به ترتیب پیشنهاد) | وضعیت پرداخت رمزارزی | وضعیت قیمت | مدرک کلیدی |
|---|---|---|---|---|---|
| **PS4/PS5 — هر بازی از استور آمریکا** | گیفت‌کارت PSN US | 1) Bitrefill ($25–$250 برابر نرخ اسمی) 2) CoinGate GIFQ (کاتالوگ PS تا −13٪) 3) Cryptorefills (storefront چندکشوری) 4) Kinguin (PSN $10 با 15 پیشنهاد) | Bitrefill/Cryptorefills: VERIFIED · GIFQ: PARTIALLY (بدون USDT در فهرست) · Kinguin: NOT SUPPORTED مستقیم | PSN $25: −3٪ تا −15.6٪ (به تخفیف GIFQ وابسته)؛ $50: رد اقتصادی | bitrefill.com/…/sony-playstation-usa · coingate.com/gift-cards · kinguin.net/category/3292 |
| **PS4/PS5 — مسیر ارزان‌تر: استور ترکیه** | گیفت‌کارت PSN TR / کانال رسمی Sony | 1) MTCGAME (Authorized Reseller سونی — نرخ با استعلام) 2) Oyunfor (بررسی S02) | MTCGAME: CONTACT REQUIRED (سند تاریخی BTC/TripleA) | PS Plus TR در ایران ≈ −15.8٪ اندیکاتیو → پتانسیل بالاترین | mtcgame.com/page/partnership |
| **PS4/PS5 — کد مستقیم بازی کنسولی** | کد استور از کانال توزیع / مارکت‌پلیس | 1) MTCGAME 2) Kinguin (دسته‌های PS4/PS5) 3) CodesWholesale (40,000+ محصول؛ جزئیات کنسول نیازمند استعلام) | هیچ‌کدام مستقیم رمزارزی تأییدنشده (CodesWholesale: تسویه فقط EUR) | عمومی منتشر نشده — CONTACT REQUIRED | codeswholesale.com (تأیید مستقیم 2026-11-21) |
| **Xbox — بازی‌ها و Game Pass** | کد استور/اشتراک | 1) MTCGAME (Xbox Games + Game Pass در کاتالوگ) 2) Gamivo (GPU 12M EU €125–133) 3) Kinguin 4) GIFQ (Xbox تا −4٪) | Gamivo: USDT رسمی از Q4 2022 · بقیه: نامشخص | GPU 12M EU بدون SKU مشابه ایران — نیازمند استعلام | mtcgame.com · gamivo.co بیانیه USDT |
| **Nintendo — بازی‌های eShop** | گیفت‌کارت eShop US | 1) Bitrefill 2) Cryptorefills 3) GIFQ (Nintendo تا −10٪) 4) Kinguin | مانند ردیف PSN | eShop US $50: رد اقتصادی (+15.9٪) — فقط برای «دسترسی» بخرید نه سود قیمتی | IRAN-MARKET-PRICING.md SKU S02-2 |
| **PC/Steam (مکمل کاتالوگ)** | کلید استیم | 1) CodesWholesale (پلکانی + API dropshipping) 2) Kinguin (ESA API) 3) Gamivo | NOT SUPPORTED / مستقیم ندارد | tiered pricing — نرخ پس از ثبت‌نام | codeswholesale.com · kinguin.net/dev-portal |
| **اکانت ظرفیتی / Primary-Secondary** | اشتراک اکانت PSN | فقط GGSel و FunPay (C2C روسی) | FunPay: USDT TRC20 PARTIALLY | ارزان‌ترین ولی ریسک بلاک/چارج‌بک | نقض ToS سونی [ردشده به‌عنوان تأمین قانونی] |

## رتبه «پشتیبانی بازی» (از میان ۹ پرونده کامل S01 + موارد S02)

1. **Kinguin** — تنها تأمین‌کننده با پوشش همزمان: دسته‌های بازی PS4/PS5/Xbox/Nintendo + کارت‌های PSN + Purchase API. مانع: پرداخت رمزارزی مستقیم ندارد.
2. **MTCGAME** — کاتالوگ Xbox Games/Game Pass/Nintendo + کانال رسمی Sony برای PSN؛ جغرافیای ترکیه؛ همه چیز با استعلام.
3. **Bitrefill / Cryptorefills** — کاتالوگ «کیف پول» تمیز با USDT و API؛ برای فروش بازی از مسیر استور، نه کلید مستقیم.
4. **CoinGate GIFQ** — دامنه PS/Xbox/Nintendo/Steam با تخفیف کاتالوگ و API عمده؛ USDT نیازمند تأیید.
5. **CodesWholesale** — عظیم‌ترین کاتالوگ کلید/گیفت‌کارت با API بدون کمیسیون؛ مانع اصلی: تسویه فقط بانکی EUR [تأیید مستقیم 2026-11-21].
6. **Gamivo** — کلیدهای EU و GPU با USDT؛ بدون API خریدار.
7. **GGSel / FunPay** — فقط برای مدل ظرفیتی؛ ریسک ToS صریح؛ توصیه S01: از «منبع تأمین» حذف شود.

## گام عملی پیشنهادی برای محصولات «بازی»

1. استعلام MTCGAME: لیست عمده PSN (US/TR) و Xbox Games/Game Pass + روش پرداخت (USDT؟) — اولویت ۱.
2. استعلام GIFQ: نرخ واقعی per-SKU با تخفیف اعلامی PS تا −13٪ + تأیید USDT — اولویت ۲.
3. ثبت‌نام Partner در Bitrefill و API در Cryptorefills برای خط تأمین پشتیبان با USDT — اولویت ۳.
4. CodesWholesale: ساخت اکانت رایگان و پرسش از support@codeswholesale.com درباره تسویه غیر EUR و کاتالوگ کنسولی — اولویت ۴.
5. Kinguin: فقط اگر راه‌حل پرداخت مستقیم/پذیرش نهاد ایرانی تأیید شد.
6. دسته ظرفیتی: تصمیم کارفرما (توصیه: حذف از منابع؛ اگر ماند، فقط خرید آزمایشی + ضمانت مکتوب).

## محدودیت‌های ثبت‌شده در این جلسه

- مسیر PSN-TR در Cryptorefills: URLهای امتحان‌شده 404/timeout شدند → [نیازمند استعلام].
- صفحه digital-wholesale کینگ‌وین و آکاردئون‌های MTCGAME محتوا ندادند → جزئیات عمده [نیازمند استعلام].
- هیچ قیمت عمده واقعی هنوز دریافت نشده (مکاتبات منتظر تأیید کارفرما هستند).
