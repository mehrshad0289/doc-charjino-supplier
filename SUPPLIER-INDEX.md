# SUPPLIER-INDEX — فهرست تأمین‌کنندگان

> آخرین به‌روزرسانی: 2026-11-21 — **نسخه ادغام‌شده دو جلسه موازی** (S01: فاز ۱+۲ با جستجوی وب موازی؛ S02: فاز ۱ + قالب‌های Word). قبل از بررسی هر اسلاگ، تاریخچه گیت را ببینید تا کار تکراری نشود.

## راهنما

- **وضعیت**: `Lead` / `Screened` / `Deep-Dive` / `Profile` (پروفایل سبک) / `Contact-Req` / `Rejected` / `Reference` (فقط مبنای قیمت ایران)
- **رمزارز**: `VERIFIED` / `PARTIALLY VERIFIED` / `CONTACT REQUIRED` / `NOT SUPPORTED` / `UNKNOWN`
- **بررسی**: S01 / S02 = جلسه‌ای که مسئولیت بررسی را برداشته است.

## جدول غربالگری (ادغام‌شده)

| # | Slug | نام | کشور | دسته | رمزارز | API | وضعیت | بررسی |
|---|---|---|---|---|---|---|---|---|
| 1 | bitrefill | Bitrefill (Airfill Prepaid AB) | سوئد | گیفت‌کارت PSN/Xbox/Nintendo/Steam چند ریجن | VERIFIED (BTC, Lightning, ETH, USDT, USDC, LTC…) | docs.bitrefill.com (Business/Partner) | Deep-Dive | S01 |
| 2 | cryptorefills | Cryptorefills | هلند (KvK 63338149) | PSN/Nintendo/Xbox/UniPin — 180+ کشور | VERIFIED (USDT-Tron صریح، USDC-Solana، 20+) | REST v4/v5 + webhooks، بدون KYC | Deep-Dive | S01 |
| 3 | coingate-gifq | CoinGate Gift Cards (GIFQ) | لیتوانی | PSN/Xbox/Nintendo/Steam/Razer — 90+ کشور | PARTIALLY VERIFIED (BTC/ETH/70+؛ USDT در صفحه مشاهده نشد) | docs.gifq.com + sandbox + volume pricing | Deep-Dive | S01 |
| 4 | kinguin | Kinguin Digital Wholesale | لهستان / نهاد HK | کلید بازی + گیفت‌کارت | PARTIALLY VERIFIED (مستقیم ندارد؛ غیرمستقیم از طریق گیفت‌کارت) | Purchase API (ESA) + dev-portal | Deep-Dive | S01 |
| 5 | gamivo | Gamivo | EU (مالت) | کلید بازی + اشتراک | PARTIALLY VERIFIED (BTC/BCH/ETH/USDT از Dec 2022) | Seller API | Deep-Dive | S01 |
| 6 | mtcgame | MTCGAME | ترکیه | اپین/گیفت‌کارت — ادعای توزیع‌کننده رسمی PlayStation از 2007 | CONTACT REQUIRED (تاریخچه BTC/TripleA) | Reseller/API با فرم تماس | Deep-Dive | S01 |
| 7 | codeswholesale | CodesWholesale | Summanus LTD LC | 40,000+ محصول دیجیتال B2B | NOT SUPPORTED (تسویه EUR بانکی) | docs.codeswholesale.com | Deep-Dive | S02 (پروفایل سبک S01) |
| 8 | coinsbee | Coinsbee | نامشخص | 5000+ گیفت‌کارت | PARTIALLY VERIFIED (S02: ادعای USDT TRC-20 صریح؛ S01: شبکه‌ها در صفحه مشخص نبود و PSN ناموجود بود) | ندارد | Deep-Dive | S02 |
| 9 | oyunfor | Oyunfor | ترکیه (Kuşadası) | Epin/گیفت‌کارت TR | UNKNOWN | پنل همکاری (İş Ortaklığı) | Deep-Dive | S02 |
| 10 | funpay | FunPay | روسیه | C2C اکانت/کلید/تاپ‌آپ | PARTIALLY VERIFIED (USDT TRC20) | پنل فروشنده | Deep-Dive — ریسک ToS اکانت‌ها + گزارش بلوکه شدن موجودی (S01) | S02 |
| 11 | ggsel | GGsel | روسیه | مارکت‌پلیس اکانت PSN | UNKNOWN | ندارد | Deep-Dive — اکانت‌ها = نقض ToS سونی، هیچ تأمین قانونی ندارد | S02 |
| 12 | seagm | SEAGM | مالزی | گیفت‌کارت/تاپ‌آپ جهانی | VERIFIED (BTC/ETH/USDT via TripleA؛ بازگشت وجه رمزارزی صفر) | ندارد | Profile | S01 |
| 13 | offgamers | OffGamers | مالزی | گیفت‌کارت/تاپ‌آپ جهانی + reseller@offgamers.com | VERIFIED (BTC، USDT-ETH، USDT-Polygon؛ بازگشت = اعتبار فروشگاه) | ندارد | Profile | S01 |
| 14 | turgame | Turgame B2B | نامشخص (احتمالاً ترکیه) | گیفت‌کارت دیجیتال bulk | UNKNOWN | JSON API | Profile | S01 |
| 15 | genba-digital | Genba Digital | نامشخص | توزیع رسمی کلید بازی (220+ publisher) | UNKNOWN | API (تأیید غیررسمی) | Screened — onboarding محدود | S01 |
| 16 | genghis | Genghis.pro | نامشخص (جدید) | 4500+ گیفت‌کارت | PARTIALLY VERIFIED (USDT-Tron صریح، 300+ کوین) | /developers تأییدنشده | Screened — فروشگاه جدید | S01 |
| 17 | cardexpress-eg | CardExpress Egypt | مصر | 500+ برند B2B | UNKNOWN | API | Screened — نشانه اعتبار ضعیف | S01 |
| 18 | rewarble | Rewarble | نامشخص | کوپن گیمینگ چندمنظوره | غیرمستقیم | ندارد | Screened | S01 |
| 19 | reloadly | Reloadly | اسپانیا | Gift Card API 200+ برند | NOT SUPPORTED (شارژ رمزارزی مستند نشده) | developers.reloadly.com | Screened | هر دو |
| 20 | unipin | UniPin | اندونزی | تاپ‌آپ/واوچر | NOT SUPPORTED | dev-api.unipin.com | Screened | S01 |
| 21 | startselect | Startselect | هلند | گیفت‌کارت رسمی | NOT SUPPORTED (PayPal/Klarna) | — | Screened | S01 |
| 22 | xoxoday | Xoxoday Plum | هند | گیفت‌کارت rewards | UNKNOWN | developers.xoxoday.com | Screened — نگرانی ممنوعیت resale | هر دو |
| 23 | razer-gold | Razer Gold (رسمی) | سنگاپور | ریزر گلد | UNKNOWN | — | Screened (خرید غیرمستقیم ممکن) | S01 |
| 24 | onecard-bitaqaty | OneCard / Bitaqaty | عربستان | کارت دیجیتال MENA | UNKNOWN | Reseller API v2 (v2docs.onecard.com) | Screened — سایت از S01 در دسترس نبود | هر دو |
| 25 | play-asia | Play-Asia | هنگ‌کنگ | کد دیجیتال/فیزیکی | UNKNOWN | ندارد (Partner Program) | Screened | S02 |
| 26 | bynogame | ByNoGame | ترکیه | Epin/skin از 2007 | UNKNOWN | Bayilik + API | Screened | S02 |
| 27 | plati-digiseller | Plati.market / Digiseller | روسیه | مارکت‌پلیس C2C + Digiseller API | UNKNOWN (گزارش پرداخت رمزارزی خریداران) | api.digiseller.com | Screened — ریل روسی + منشأ گری | هر دو |
| 28 | g2a | G2A | لهستان | مارکت‌پلیس کلید | NOT SUPPORTED (مشاهده نشد) | Integration API فروشنده (فقط کسب‌وکار ثبت‌شده) | Screened | S01 |
| 29 | eneba | Eneba | لیتوانی | مارکت‌پلیس کلید | غیرمستقیم فقط | Seller API (integrations@eneba.com) | Screened | هر دو |
| 30 | k4g | K4G | لهستان | فروشگاه/مارکت‌پلیس | NOT VERIFIED | Seller API | Screened | S01 |
| 31 | g2g | G2G | سنگاپور | C2C تاپ‌آپ | رمزارز/Binance Pay (راهنمای پرداخت) | ندارد | Screened | S01 |
| 32 | perdigital | Perdigital | ترکیه | کلید/اپین | UNKNOWN | API (سایت 403 در S01) | Screened | S01 |
| 33 | mintroute | Mintroute | MENA (نامشخص) | توزیع گیفت‌کارت | UNKNOWN | UNKNOWN | Screened — TLS منقضی، شواهد دست‌دوم | S01 |
| 34 | driffle | Driffle | نامشخص | بازی/گیفت‌کارت | UNKNOWN | UNKNOWN | Screened — صفحه Wholesale دارد | S01 |
| 35 | lekayi | Lekayi (乐卡益) | چین | کارت مجازی 3000+ SKU | UNKNOWN (رمزارز در چین ممنوع) | OpenAPI | Screened — انطباق پایین | S01 |
| 36 | ezcards | ezcards.io | نامشخص | eGift + کد بازی API | UNKNOWN | دارد | Lead | S02 |
| 37 | justacode | JustACode | نامشخص | کارت دیجیتال B2B API | UNKNOWN | دارد | Lead | S02 |
| 38 | mana-minds | Mana Minds | نامشخص | آگریگیتور Game Pass/گیفت‌کارت | UNKNOWN | نامشخص | Lead | S02 |
| 39 | mcdvideogames | MCD Video Games | نامشخص | eShop US عمده | UNKNOWN | ندارد | Lead | S02 |
| 40 | psnwholesale | PSN Wholesale Guide | نامشخص | گیفت‌کارت PSN عمده (min $500 ادعا) | UNKNOWN | ندارد | Lead — اعتبارسنجی نشده | S02 |
| 41 | zbt | ZBT | چین | دارایی دیجیتال بازی | UNKNOWN (تسویه USDT محتمل) | نامشخص | Contact-Req — سایت under maintenance در S02 | S02 |
| 42 | alibaba-topup | Alibaba Top-up Suppliers | چین | کانال عمده با مذاکره | نامشخص | — | Contact-Req | S02 |
| 43 | tillo | Tillo | بریتانیا | گیفت‌کارت 5000+ برند API | UNKNOWN | دارد | Screened — نگرانی ممنوعیت resale | S02 |
| 44 | zeusx | ZeusX | نامشخص | اکانت/آیتم بازی | UNKNOWN | ندارد | Lead — ریسک ToS | S02 |
| 45 | wholesale-digital-key | Wholesale Digital Key | نامشخص | ادعای توزیع B2B | UNKNOWN | ادعای API | Lead — S01 آن را در خوشه SEO بدون نهاد حقوقی دید | هر دو |
| 46 | brolexy | Brolexy | نامشخص | کلید/گیفت‌کارت | UNKNOWN | نامشخص | Lead — ایمیل Gmail در S01 = نشانه ضعیف | هر دو |
| 47 | foxreload | FoxReload | نامشخص (روسی‌زبان) | آگریگیتور 160k محصول | UNKNOWN | REST API | Rejected فعلاً — نهاد حقوقی منتشرنشده، © 2026 | هر دو |
| 48 | difmark | Difmark | UK/قبرس | مارکت‌پلیس C2C | رمزارز دارد | ندارد | Rejected — اتهامات کلاهبرداری (Reddit/Trustpilot) | S01 |
| 49 | mercury | Mercury Digital | اسرائیل | توزیع کلید B2B | UNKNOWN | ندارد | Rejected — اصطکاک قضایی + پیش‌پرداخت اجباری | S01 |
| 50 | xsolla | Xsolla | آمریکا | زیرساخت پرداخت | محدودیت سرزمین‌های تحریمی صریح | developers.xsolla.com | Rejected — ریسک انطباقی صریح | S01 |
| 51 | seo-cluster | wholesaledigitalkey / Padzup / GameKeyDistribution / FazerCards | نامشخص | ادعای توزیع B2B | UNKNOWN | UNKNOWN | Rejected — صفحات SEO بدون نهاد/قیمت/سابقه | S01 |
| 52 | psn-bazaar | PSN Bazaar (تلگرام) | نامشخص | ادعای «50٪ تخفیف» | UNKNOWN | — | Rejected — غیرقابل اعتبارسنجی | S02 |
| 53 | tango-giftbit | Tango / Giftbit / Tremendous | آمریکا | پاداش سازمانی | UNKNOWN | دارد | Rejected برای resale بدون استعلام | S02 |
| 54 | playerauctions | PlayerAuctions | نامشخص | اکانت PS4/PS5 | UNKNOWN | — | Screened — ریسک ToS (اکانت‌ها) | هر دو |
| 55 | giftcard-go | GiftCard Go | ایران | گیفت‌کارت عمده | — | — | Reference (مبنای مقایسه داخلی) | S02 |
| 56 | pspro | PSPRO | ایران | گیفت‌کارت + PS Plus | — | — | Reference | هر دو |
| 57 | digikala | Digikala | ایران | گیفت‌کارت خرده | — | — | Reference — در S01 لیست مستقیم این SKUها را نشان نداد | هر دو |
| 58 | pcbaz | PC Baz | ایران | گیفت‌کارت Xbox US/UK | — | — | Reference — 504 در S01 | هر دو |
| 59 | iran-shops | Digi720 / GiftcardStore / Gamalop / Cardtak / CDKeY / Giftro / Emalls / Torob | ایران | منابع قیمت SKUهای بنچمارک | — | — | Reference — قیمت‌ها در IRAN-MARKET-PRICING.md | S01 |

## نتیجه غربالگری — تقسیم کار بین جلسات

- **S01 بررسی عمیق می‌کند (۶ مورد)**: Bitrefill، Cryptorefills، CoinGate GIFQ، Kinguin، Gamivo، MTCGAME + پروفایل سبک SEAGM، OffGamers، Turgame.
- **S02 اعلام Deep-Dive کرده (۵ مورد)**: CodesWholesale، Coinsbee، Oyunfor، FunPay، GGsel — این‌ها از سهم S01 خارج شدند.
- **نتیجه کلیدی فاز ۲**: پرداخت رمزارزی مستقیم + API با بهترین شواهد: **Cryptorefills (USDT-TRON صریح)**، **Bitrefill (USDT/BTC/LTC)**، **CoinGate GIFQ (0% کارمزد رمزارزی، sandbox)**.

هشدار ریسک: psnwholesale.com و alphapsn.ltd فقط snippet — بدون رجیستر/مجوز. [ردشده فعلاً]

محصولات «ظرفیت ۱/۲/۳» و اکانت‌های Primary/Secondary رایج بازار ایران مبتنی بر اشتراک‌گذاری اکانت PSN هستند. بررسی مستند (Session 01، رشته C): **هیچ تأمین‌کننده رسمی/قانونی بین‌المللی برای این دسته وجود ندارد** — PSN ToS (مارس ۲۰۲۵) خرید/فروش/اشتراک‌گذاری اکانت را صریحاً ممنوع می‌کند و ممنوعیت Reseller (§8.4) و خاتمه غیرقابل بازگشت (§12.3) با لینک playstation.com مستند شده است. هرگونه تأمین‌کننده اکانت بدون اثبات منشأ قانونی، برچسب `[ردشده]` یا `[نیازمند استعلام]` می‌گیرد.
