# فهرست تأمین‌کنندگان (SUPPLIER-INDEX)

> آخرین به‌روزرسانی: 2026-11-21 — فاز ۲ (غربالگری) انجام شد. ۴۰ سرنخ از ۴ رشته جستجوی موازی (توزیع‌کنندگان B2B، پلتفرم‌های رمزارزی، مارکت‌پلیس‌ها، بازار ایران) غربال شدند.

## راهنما

- **وضعیت**: `Lead` (سرنخ) / `Screened` (غربال‌شده، بررسی سطحی) / `Deep-Dive` (بررسی عمیق + پروفایل Word) / `Rejected` (ردشده)
- **رمزارز**: `VERIFIED` (با مدرک از صفحه رسمی) / `PARTIALLY VERIFIED` / `CONTACT REQUIRED` / `NOT SUPPORTED` / `UNKNOWN`

## جدول غربالگری

| # | Slug | نام | کشور | دسته | B2B/عمده | رمزارز | API | امتیاز اولیه | وضعیت |
|---|---|---|---|---|---|---|---|---:|---|
| 1 | bitrefill | Bitrefill | سوئد (Airfill Prepaid AB) | گیفت‌کارت PSN/Xbox/Nintendo/Steam چند ریجن | Partner/Business Program | VERIFIED (BTC, Lightning, ETH, USDT, USDC, LTC, DOGE…) | docs.bitrefill.com | 88 | Deep-Dive |
| 2 | cryptorefills | Cryptorefills | هلند (KvK 63338149) | PSN/Nintendo/Xbox/UniPin — 180+ کشور | API B2B بدون پیش‌پرداخت | VERIFIED (USDT-Tron, USDC-Solana, BTC, LTC, 20+) | REST+webhooks (v4/v5) | 86 | Deep-Dive |
| 3 | coingate-gifq | CoinGate Gift Cards (GIFQ) | لیتوانی (UAB Rewards distributed) | PSN/Xbox/Nintendo/Steam/Razer — 90+ کشور | Volume pricing 10→10000 کارت | PARTIALLY VERIFIED (BTC/ETH/70+ کوین، USDC؛ USDT در صفحه مشاهده نشد) | docs.gifq.com + sandbox | 82 | Deep-Dive |
| 4 | kinguin | Kinguin Digital Wholesale | لهستان / شرکت HK | کلید بازی + گیفت‌کارت | Wholesale tier + Purchase API | PARTIALLY VERIFIED (پرداخت مستقیم رمزارز ندارد؛ فقط از طریق گیفت‌کارت Kinguin خریداری‌شده با رمزارز) | Purchase API (ESA) + dev-portal | 78 | Deep-Dive |
| 5 | gamivo | Gamivo | اتحادیه اروپا (مالت) | کلید بازی + اشتراک | فروشندگان API دارند؛ خریدار عمده نیست | PARTIALLY VERIFIED (BTC/BCH/ETH/USDT از 2022) | Seller API | 72 | Deep-Dive |
| 6 | mtcgame | MTCGAME | ترکیه | اپین/گیفت‌کارت/اشتراک — ادعای توزیع‌کننده رسمی PlayStation از 2007 | بله — «Reseller and API Requests» در صفحه تماس | CONTACT REQUIRED (تاریخچه BTC با TripleA؛ وضع فعلی نامشخص) | API به‌صورت موردی برای Reseller | 75 | Deep-Dive |
| 7 | seagm | SEAGM | مالزی | گیفت‌کارت/تاپ‌آپ جهانی | عمده عمومی ندارد | VERIFIED (BTC/ETH/USDT via TripleA؛ بازگشت وجه رمزارزی = صفر) | ندارد | 65 | Profile |
| 8 | offgamers | OffGamers | مالزی | گیفت‌کارت/تاپ‌آپ جهانی | عمده عمومی ندارد | VERIFIED (BTC، USDT-ETH، USDT-Polygon؛ بازگشت = اعتبار فروشگاه) | ندارد | 64 | Profile |
| 9 | codeswholesale | CodesWholesale | Summanus LTD LC (نامشخص) | 40,000+ محصول دیجیتال | B2B Marketplace + tiered pricing | NOT SUPPORTED (تسویه بانکی EUR) | docs.codeswholesale.com (403 هنگام بررسی) | 58 | Profile |
| 10 | turgame | Turgame B2B | نامشخص | گیفت‌کارت PS/Xbox/Steam/Nintendo | پلتفرم Reseller + CSV | UNKNOWN (روش پرداخت منتشر نشده) | JSON API | 55 | Profile |
| 11 | genba-digital | Genba Digital | نامشخص (UK محتمل) | توزیع رسمی کلید بازی | 220+ publisher / 500+ retailer | UNKNOWN | API (تأیید غیررسمی) | 52 | Screened |
| 12 | genghis | Genghis.pro | نامشخص (جدید) | 4500+ گیفت‌کارت | خرده‌فروشی | PARTIALLY VERIFIED (300+ کوین، USDT-Tron صریح) | /developers تأییدنشده | 45 | Screened — فروشگاه جدید، اعتبار کم |
| 13 | coinsbee | Coinsbee | نامشخص | 5000+ گیفت‌کارت | خرده‌فروشی | PARTIALLY VERIFIED (250+ کوین، شبکه‌ها نامشخص) | ندارد | 48 | Screened — PSN در تاریخ بررسی ناموجود |
| 14 | cardexpress-eg | CardExpress Egypt | مصر | 500+ برند | B2B + API | UNKNOWN | API | 42 | Screened — نشانه‌های اعتبار ضعیف |
| 15 | rewarble | Rewarble | نامشخص | کوپن چندمنظوره گیمینگ | از طریق مارکت‌ها | غیرمستقیم (با BTC/CoinGate قابل خرید) | ندارد | 40 | Screened |
| 16 | reloadly | Reloadly | اسپانیا | Gift Card API 200+ برند | API B2B | NOT SUPPORTED (شارژ کیف پول رمزارزی مستند نشده) | developers.reloadly.com | 42 | Screened |
| 17 | unipin | UniPin | اندونزی | تاپ‌آپ/واوچر بازی | Developer Portal | NOT SUPPORTED | dev-api.unipin.com | 40 | Screened |
| 18 | startselect | Startselect | هلند | گیفت‌کارت رسمی | B2B | NOT SUPPORTED (Apple Pay/PayPal/Klarna) | ندارد | 30 | Screened |
| 19 | xoxoday | Xoxoday | هند | Giftcard API | B2B rewards | UNKNOWN | developers.xoxoday.com | 32 | Screened |
| 20 | onecard | OneCard | عربستان | گیفت‌کارت منطقه MENA | نامشخص | UNKNOWN (سایت از محیط ما در دسترس نبود) | ندارد | 30 | Screened — نیازمند دسترسی مستقیم |
| 21 | cryptovoucher | CryptoVoucher.io | نامشخص | کوپن خرید رمزارز | — | N/A (ورودی فیات) | ندارد | 20 | Screened — خارج از هدف |
| 22 | razer-gold | Razer Gold (رسمی) | سنگاپور | ریزر گلد | Reseller program نامشخص | UNKNOWN | — | 35 | Screened (خرید غیرمستقیم از Bitrefill/Genghis ممکن است) |
| 23 | g2a | G2A | لهستان | مارکت‌پلیس کلید | فقط برای کسب‌وکار ثبت‌شده (سمت فروشنده) | NOT SUPPORTED (مشاهده نشد) | Integration API فروشنده | 45 | Screened |
| 24 | eneba | Eneba | لیتوانی | مارکت‌پلیس کلید | Sell-on-Eneba | غیرمستقیم فقط | Seller API | 42 | Screened |
| 25 | k4g | K4G | لهستان | فروشگاه/مارکت‌پلیس | لیست‌کردن محصول با API | NOT VERIFIED | Seller API | 40 | Screened |
| 26 | difmark | Difmark | UK/قبرس | مارکت‌پلیس C2C | ندارد | رمزارز دارد اما اتهامات جدی کلاهبرداری | ندارد | 15 | Rejected — ریسک بالا |
| 27 | plati-market | Plati.market | روسیه | مارکت‌پلیس C2C | Digiseller | رمزارز (گزارش خریداران) | plati.market/api | 35 | Screened — ریجن گری + ریل روسی |
| 28 | funpay | FunPay | روسیه | C2C اکانت‌ها | ندارد | NOT VERIFIED | ندارد | 22 | Screened — گزارش بلوکه شدن موجودی فروشندگان |
| 29 | g2g | G2G | سنگاپور | C2C تاپ‌آپ | فروشنده از 4.99% | رمزارز/Binance Pay در راهنمای پرداخت | ندارد | 38 | Screened |
| 30 | foxreload | FoxReload | نامشخص (روسی‌زبان) | آگریگیتور 160k محصول | Reseller | UNKNOWN | REST API + sandbox | 25 | Rejected فعلاً — نهاد حقوقی منتشرنشده، © 2026 |
| 31 | digiseller | Digiseller | روسیه | CMS فروشندگی | آژانسی | UNKNOWN | دارد | 20 | Rejected — ریل روسی + منشأ گری |
| 32 | mercury | Mercury Digital | اسرائیل | توزیع کلید B2B | بله | UNKNOWN | ندارد | 18 | Rejected — اصطکاک قضایی برای خریدار ایرانی، پیش‌پرداخت اجباری |
| 33 | xsolla | Xsolla | آمریکا | زیرساخت پرداخت بازی | Reseller | محدودیت سرزمین‌های تحریمی صریح | developers.xsolla.com | 15 | Rejected — ریسک انطباقی صریح برای ایران |
| 34 | lekayi | Lekayi (乐卡益) | چین | کارت‌های مجازی 3000+ SKU | B2B | UNKNOWN (رمزارز در چین ممنوع) | OpenAPI | 25 | Screened — انطباق پایین |
| 35 | perdigital | Perdigital | ترکیه | کلید/اپین | Reseller API | UNKNOWN | API (سایت 403 هنگام بررسی) | 30 | Screened — نیازمند بررسی مجدد |
| 36 | mintroute | Mintroute | MENA (دبی؟ نامشخص) | توزیع گیفت‌کارت | نامشخص | UNKNOWN | UNKNOWN | 20 | Screened — گواهی TLS منقضی، شواهد دست دوم |
| 37 | driffle | Driffle | نامشخص | بازی/گیفت‌کارت | صفحه Wholesale دارد | UNKNOWN | UNKNOWN | 30 | Screened — شواهد عمومی کم |
| 38 | seo-cluster | wholesaledigitalkey / Padzup / Brolexy / GameKeyDistribution / FazerCards | نامشخص | ادعای توزیع B2B | ادعایی | UNKNOWN | UNKNOWN | 10 | Rejected — صفحات SEO بدون نهاد حقوقی، قیمت یا سابقه قابل اثبات |
| 39 | ggsera | GGsel / PlayerAuctions / PlayerUp / CJS CDKeys | متفرقه | مارکت‌پلیس اکانت PSN | C2C | متفاوت | ندارد | — | Rejected برای «تأمین عمده» — اکانت = نقض ToS سونی |
| 40 | iran-capacity | فروشندگان ایرانی ظرفیت‌دار (WestGameStore, IRAN Game, pspro, …) | ایران | ظرفیت ۱/۲/۳ | اشتراکی | — | — | — | تحلیل ساختار بازار — تعریف ظرفیت‌ها در IRAN-MARKET-PRICING.md |

## نتیجه غربالگری: ۶ گزینه بررسی عمیق

1. **Bitrefill** — پرداخت رمزارزی VERIFIED + API تجاری + PSN آمریکا با قیمت نقدی
2. **Cryptorefills** — USDT-TRON صریح + API بدون KYC + تسویه per-order
3. **CoinGate GIFQ** — API با Sandbox + قیمت‌گذاری پلکانی عمده + 0% کارمزد رمزارزی
4. **Kinguin Wholesale** — قدیمی‌ترین مارکت + Purchase API + قیمت PSN $10 زیر نرخ نقدی ($8.83)
5. **Gamivo** — پرداخت USDT تأییدشده + کلیدهای EU (Game Pass 12M €125-133)
6. **MTCGAME** — ترکیه + ادعای توزیع‌کننده رسمی PlayStation + مسیر Reseller/API

پروفایل سبک Word برای: SEAGM، OffGamers، CodesWholesale، Turgame.
