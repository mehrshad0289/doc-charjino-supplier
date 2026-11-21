# EVIDENCE — Bitrefill (جمع‌آوری: 2026-11-21)

هر شاهد با لینک مستقیم و برچسب. هیچ ادعایی بدون لینک در این پرونده مجاز نیست.

## پرداخت رمزارزی (VERIFIED)
- مستندات API Overview: «The Bitrefill API lets you programmatically purchase gift cards, mobile top-ups, and eSIMs. Use Bitcoin, Lightning, Ethereum, USDC, USDT, or your account balance...» — https://docs.bitrefill.com/docs/api-overview [تأییدشده با منبع]
- صفحه محصول PSN USA: «Choose the cryptocurrency you want to use for payment, such as Bitcoin, Bitcoin Lightning, Ethereum, USDT, USDC, Litecoin, Dogecoin or Dash» — https://www.bitrefill.com/us/en/gift-cards/sony-playstation-usa [تأییدشده با منبع]
- صفحه Integrate/Business API: «Add balance via crypto deposit» و «bulk gift card issuance» و «full access to Bitrefill's product catalog» — https://www.bitrefill.com/integrate/ [تأییدشده با منبع]

## قیمت‌ها (نرخ اسمی)
- PSN Store USA: مقادیر 30/50/200/250 USD و «50 USD $50.00» — همان صفحه [مشاهده‌شده در وب‌سایت]
- Nintendo eShop USA: مقادیر 50/70/100/150/200 USD با «50 USD $50.00» — https://www.bitrefill.com/us/en/gift-cards/nintendo-usa [مشاهده‌شده در وب‌سایت]

## نرخ ارز مرجع
- USDT/Toman = 272,264 (ask) — Wallex API `api.wallex.ir/v1/markets?symbol=USDTTMN` ساعت ~21:40 تهران [تأییدشده با منبع]
- USD/TRY = 50.5343 و USD/RUB = 82.0218 — open.er-api.com/v6/latest/USD [تأییدشده با منبع]

## قیمت‌های بازار ایران (SKUهای مقایسه)
- کاسپین گیفت PSN US $50 = 13,000,000 تومان (ترب)؛ YungCenter = 13,620,600؛ NICGift = 9,672,000 [مشاهده‌شده در نتایج جستجو]
- eShop US $50: Torob 12,632,500؛ وب گیفت 12,100,000؛ گیفت پرشیا 11,213,000 [مشاهده‌شده در وب‌سایت]
- محاسبات: scripts/fx_economics.py — PSN $50 نهایی 13,885,464 تومان (+14.8٪ گران‌تر از میانگین ایران)

## محدودیت‌ها
- شبکه دقیق USDT (TRC20/ERC20) در اسنیپت‌ها مشخص نشد → Checkout [نیازمند استعلام]
- سیاست بازپرداخت و ضمانت کد → [نیازمند استعلام]
- صفحات محصول با WebFetch در دسترس بودند؛ صفحه psn-usa-card (مسیر قدیمی) خطای 404 داد و از مسیر رسمی sony-playstation-usa استفاده شد.
