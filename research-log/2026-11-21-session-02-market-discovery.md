# Research Log — Session 02 (2026-11-21): فاز ۱ کشف بازار

## خلاصه جلسه

- قالب‌های استاندارد Word (PROFILE + PRICE-COMPARISON) ساخته و Push شد (SHA 6db113c).
- فاز ۱ با ۴ دسته جستجوی موازی وب اجرا شد: توزیع‌کنندگان B2B کلید/گیفت‌کارت، پلتفرم‌های رمزارزی، مارکت‌پلیس‌های اکانت/کلید، منابع منطقه‌ای (ترکیه/چین/خاورمیانه) و کانال‌های ایران.
- **۳۶ سرنخ** شناسایی و ثبت شد (هدف: حداقل ۳۰). فهرست کامل با وضعیت در SUPPLIER-INDEX.md.

## یافته‌های کلیدی فاز ۱

### گروه A — توزیع‌کنندگان B2B کلید و گیفت‌کارت دارای API
| # | نام | کشور | شواهد اولیه | وضعیت اولیه |
|---|---|---|---|---|
| 1 | CodesWholesale | لهستان | «B2B Wholesale Platform… 40,000+ game keys… automate delivery with the API» — codeswholesale.com [مشاهده‌شده در وب‌سایت/اسنیپت] | SCREENED |
| 2 | Brolexy | نامشخص | B2B wholesale: game keys, prepaid gift cards, subscription codes — brolexy.com [مشاهده‌شده در اسنیپت] | LEAD |
| 3 | Turgame B2B | احتمالاً ترکیه | Digital Gift Card Wholesale + API/bulk — [مشاهده‌شده در اسنیپت] | LEAD |
| 4 | Wholesale Digital Key | نامشخص | «#1 Global B2B Game Distributor… Instant API delivery» — دامنه در اسنیپت پنهان؛ نیازمند شناسایی [نیازمند استعلام] | LEAD |
| 5 | Mana Minds | نامشخص | B2B Aggregator گیفت‌کارت و Game Pass Ultimate/Essential [مشاهده‌شده در اسنیپت] | LEAD |
| 6 | FoxReload | نامشخص | Wholesale Game Codes & Gift Card API؛ دسترسی به Reloadly — foxreload.com [مشاهده‌شده در اسنیپت] | LEAD |
| 7 | ezcards.io | نامشخص | Gift Card & Game Code API: balances, catalog, eGift delivery [مشاهده‌شده در اسنیپت] | LEAD |
| 8 | JustACode | نامشخص | Enterprise B2B API برای دیجیتال کارت [مشاهده‌شده در اسنیپت] | LEAD |
| 9 | Kinguin Digital Wholesale | لهستان | Digital Wholesale Partnership + Kinguin API (فرم integration) [مشاهده‌شده در اسنیپت] | SCREENED |
| 10 | Eneba (seller API) | لیتوانی | API integration برای فروشندگان [مشاهده‌شده در اسنیپت] | LEAD |
| 11 | GAMIVO (shop API) | هلند/لهستان؟ | «Connect your shop with GAMIVO via API» [مشاهده‌شده در اسنیپت] | LEAD |
| 12 | SEAGM | مالزی | فروشگاه جهانی + برنامه همکاری [مشاهده‌شده در اسنیپت] | SCREENED |
| 13 | OffGamers | مالزی | خرید عمده: reseller@offgamers.com + برنامه Reseller [مشاهده‌شده در اسنیپت] | SCREENED |
| 14 | Play-Asia | هنگ‌کنگ | Partner Program + بخش Digital Codes [مشاهده‌شده در اسنیپت] | SCREENED |
| 15 | OneCard / Bitaqaty | عربستان | Reseller Integration API v2 (v2docs.onecard.com) [مشاهده‌شده در اسنیپت] | SCREENED |
| 16 | ByNoGame | ترکیه | از ۲۰۰۷؛ E-Pin Bayیلیک با API و شارژ بدهی بدون کمیسیون (IBAN) [مشاهده‌شده در اسنیپت] | SCREENED |
| 17 | Oyunfor | ترکیه | İş Ortaklığı (برنامه همکاری) + فروش Epin؛ آدرس Kuşadası؛ WhatsApp رسمی [مشاهده‌شده در وب‌سایت] | SCREENED |

### گروه B — پلتفرم‌های با پرداخت رمزارزی (اولویت شرجینو)
| # | نام | شواهد پرداخت رمزارزی | وضعیت رمزارز |
|---|---|---|---|
| 18 | Bitrefill (آمریکا/سوئد) | API Overview: خرید با BTC, Lightning, Ethereum, USDC, USDT؛ Business API با شارژ موجودی از/crypto deposit — docs.bitrefill.com [تأییدشده با منبع] | VERIFIED |
| 19 | Coinsbee | صفحات PSN/Xbox: خرید با BTC/ETH/USDC/USDT/Solana و ۲۵۰+ کوین؛ اشاره صریح به USDT روی TRON (TRC-20) [تأییدشده با منبع] | VERIFIED |
| 20 | FunPay (روسیه) | سند دستورالعمل پرداخت USDT TRC20 برای کاربران FunPay؛ سرویس پرداخت رسمی [مشاهده‌شده در وب/اسناد] | PARTIALLY VERIFIED |
| 21 | Plati.market / Digiseller (روسیه) | ارزهای پنل: USD/RUB/EUR/UAH؛ API فروشنده تأییدشده (api.digiseller.com)؛ رمزارز: [نیازمند استعلام] | UNKNOWN |
| 22 | ZBT (zbt.com، چین) | «Global Gaming Digital Asset Community»؛ سایت در اسنیپت «under maintenance»؛ ارز تسویه احتمالاً USDT [نیازمند استعلام] | UNKNOWN |

### گروه C — مارکت‌پلیس‌های اکانت و کلید (دسته پرریسک)
| # | نام | شواهد | ریسک |
|---|---|---|---|
| 23 | GGSel (ggsel.net، روسیه) | کاتالوگ حجیم اکانت PSN (۱۱٬۱۴۹ اکانت، ۲۷۹ پروفایل، ۱۲٬۵۷۵ نظر) + «اجاره اکانت PSN» از ۱۴۹₽ [مشاهده‌شده در وب‌سایت] | منشأ اکانت‌ها قابل اثبات نیست؛ اجاره = الگوی نزدیک به «ظرفیت» بازار ایران |
| 24 | PlayerAuctions | خرید اکانت PS4/PS5 با گارانتی تحویل از $75 [مشاهده‌شده در اسنیپت] | ریسک ToS سونی |
| 25 | ZeusX | مارکت‌پلیس اکانت/آیتم [مشاهده‌شده در اسنیپت] | ریسک ToS |
| 26 | PSN Bazaar (تلگرام) | کانال تلگرام فروش بازی PS4/PS5 با «۵۰٪ تخفیف» [مشاهده‌شده در اسنیپت] | غیرقابل اعتبارسنجی؛ احتمال منشأ غیرمجاز — REJECTED برای تأیید بدون مدرک |

### گروه D — تجمیع‌گرهای پاداش/گیفت‌کارت B2B (معمولاً ممنوعیت فروش مجدد در ToS)
| # | نام | شواهد | نکته انطباقی |
|---|---|---|---|
| 27 | Tillo (بریتانیا) | Gift Card API با ۵٬۰۰۰+ برند، ۴۱ کشور [مشاهده‌شده در اسنیپت] | کاربرد پاداش/مشوق؛ ممنوعیت resale در شرایط ToS محتمل — [نیازمند استعلام] |
| 28 | Xoxoday Plum | فهرست شامل Steam, Razer Gold, PlayStation, Nintendo [مشاهده‌شده در اسنیپت] | همان نکته بالا |
| 29 | Reloadly | Gift Card API + مستندات رسمی (docs.reloadly.com) [تأییدشده با منبع] | پلتفرم payouts؛ درباره resale نیازمند استعلام |
| 30 | Tango/Giftbit/Tremendous/Runa/Hoppier | در رتبه‌بندی بهترین Gift Card APIهای ۲۰۲۶ [مشاهده‌شده در اسنیپت] | نگرش ممنوعیت resale — اولویت پایین |
| 31 | ezcards.io | (تکرار از گروه A) | — |

### گروه E — کانال‌ها و فروشندگان ایرانی (مبنای مقایسه بازار، نه تأمین‌کننده جهانی)
| # | نام | شواهد |
|---|---|---|
| 32 | GiftCard Go (صفحه خرید عمده) | صفحه «خرید عمده گیفت کارت» برای همکاران [مشاهده‌شده در اسنیپت] |
| 33 | PSPRO (pspro.ir) | فروش گیفت‌کارت سه کنسول [مشاهده‌شده در اسنیپت] |
| 34 | Digikala (دسته گیفت‌کارت) | قیمت خرده‌فروشی مرجع [مشاهده‌شده در اسنیپت] |
| 35 | PC Baz | گیفت‌کارت Xbox US/UK تحویل آنی [مشاهده‌شده در اسنیپت] |
| 36 | mcdvideogames.com | Wholesale Nintendo eShop US [مشاهده‌شده در اسنیپت] |
| 37 | psnwholesale.com | راهنمای B2B خرید عمده PSN با حداقل سفارش $500 [مشاهده‌شده در اسنیپت] |
| 38 | Alibaba (کانال) | تأمین‌کنندگان top-up با تسویه مورد مذاکره — [نیازمند استعلام] |

## غربالگری اولیه برای بررسی عمیق (فاز ۳)

انتخاب‌شده برای پرونده کامل (۴ فایل Word): **bitrefill، coinsbee، codeswholesale، oyunfor، funpay، ggsel**
- منطق انتخاب: پوشش هر چهار نیاز شارژینو = رمزارز تأییدشده (Bitrefill/Coinsbee)، API عمده واقعی (CodesWholesale)، ریجن ترکیه و پنل همکاری (Oyunfor)، اکانت‌ها/ظرفیت با پرداخت TRC20 (FunPay)، مقایسه بازار اکانت (GGSel).
- Kinguin، OneCard/Bitaqaty، ByNoGame، Plati/Digiseller، SEAGM/OffGamers، Play-Asia، Reloadly/Tillo: غربال‌شده، نیازمند تماس یا در فهرست انتظار بررسی عمیق جلسه بعد.
- ZBT: به دلیل نامشخص بودن وضعیت سایت/تسویه در این جلسه، در وضعیت [نیازمند استعلام] ماند.

## محدودیت‌های ثبت‌شده

- ارسال پیام تجاری به هیچ تأمین‌کننده‌ای بدون تأیید صاحب کسب‌وکار انجام نمی‌شود؛ برای همه پرونده‌ها CONTACT-HISTORY با پیش‌نویس پیام تهیه می‌شود.
- برخی دامنه‌ها در اسنیپت‌های جستجو ماسک شده‌اند (Wholesale Digital Key، Mana Minds) و باید در فاز بررسی عمیق شناسایی شوند.
- محصولات «ظرفیت» و اجاره اکانت: هیچ تأمین‌کننده رسمی بین‌المللی با منشأ قابل اثبات یافت نشد؛ این یافته صادقانه ثبت شد و تمام گزینه‌های این دسته با وضعیت [نیازمند استعلام] و ریسک ToS بالا مستند می‌شوند.
