# DECISIONS — تصمیم‌ها و پیشنهاد عملیاتی (2026-11-21)

## پاسخ‌های صریح مأموریت

| سؤال | پاسخ |
|---|---|
| از کدام تأمین‌کننده بخریم؟ | ترکیبی: **SEAGM (Partner Alliance)** + **CoinGate GIFQ (wholesale)** برای کارت/اشتراک با USDT؛ **Bitrefill (Partner)** برای اتوماسیون کاتالوگ و رفاند امن؛ **MTCGame (wholesale@)** برای مذاکره حجمی؛ **Plati/Digiseller** فقط مشروط برای اکانت‌های ظرفیت‌دار با پذیرش ریسک. |
| چرا؟ | تنها گزینه‌هایی که هم‌زمان: کاتالوگ PS/Xbox/Nintendo + مسیر پرداخت رمزارزی مستند + برنامه B2B/API واقعی دارند. جزئیات و شواهد در PROFILE هرکدام. |
| چقدر ارزان‌تر از بازار ایران؟ | **در حالت خرده‌فروی هیچ‌کدام ارزان‌تر نیستند** (PSN US $100: Bitrefill/MTCGame ≈ +0.15٪ نسبت به میانگین ۳ فروشنده ایرانی = 26,857,000 تومان). اقتصادی‌شدن منوط به تیر عمده GIFQ/SEAGM/MTCGame است — این عدد پس از استعلام فاز ۶ تکمیل می‌شود. [تأییدشده با منبع + تخمین] |
| پرداخت با چه رمزارزی؟ | **USDT TRC20** (کم‌کارمزدترین) در Bitrefill/Cryptorefills/Coinsbee/CoinGate؛ USDT ERC20/Polygon در Bitrefill/G2G؛ BEP20 عملاً در هیچ مستند رسمی تأیید نشد. |
| حداقل مبلغ؟ | GIFQ از ۱۰ کارت؛ OffGamers هدف فروش ماهانه $1,000؛ Bitrefill بدون اکانت $500/روز؛ بقیه [نیازمند استعلام]. |
| چطور سفارش ثبت کنیم؟ | مسیر API در API-DOCUMENTATION هرکدام (SEAGM HMAC، Digiseller SHA256، GIFQ REST، Bitrefill Partner)؛ مسیر پنل/ایمیل در CONTACT-HISTORY. |
| چگونه محصول را دریافت کنیم؟ | کد دیجیتال فوری ایمیل/پنل؛ اکانت‌ها از مارکت‌پلیس با escrow (Eldorado TradeShield / G2G) یا unique-code (Digiseller). |
| آیا API دارد؟ | SEAGM، Digiseller، G2G، Kinguin، GIFQ، Bitrefill، Cryptorefills: بله (لینک مستندات در API-SUPPLIERS.md)؛ MTCGame/OffGamers: روی درخواست. |
| چه ریسک‌هایی؟ | تحریم/انطباق (هیچ پلتفرمی پذیرش رسمی ایران را مستند نکرده؛ Eneba ممنوع)، بن اکانت‌ها (ToS سونی)، رفاند پس از تحویل (CoinGate)، KYC (CoinGate >€700، Coinsbee >€1000). |
| حاشیه سود؟ | تکی: صفر/منفی؛ عمده: بسته به تخفیف — فرمول محاسبه در PROFILE §۱۹ هر تأمین‌کننده با نرخ 268,970 (tgju 2026-11-21). |

## بهترین‌ها به تفکیک دسته

- بهترین PSN/Xbox/Nintendo کارت با crypto: **Bitrefill** / **CoinGate GIFQ**
- بهترین B2B/API: **SEAGM** (تنها API کامل + Partner + crypto)
- بهترین قیمت (اکانت/ظرفیت): **Plati+Digiseller** — مشروط و پرریسک
- بهترین بدون crypto: **MTCGame** (مذاکره انسانی)
- بهترین گزینه کلی برای شارژینو: **SEAGM** و بعد **GIFQ** — به شرط پاسخ مثبت استعلام عمده/انطباق.

## اقدام فوری پیشنهادی (پس از تأیید کارفرما)
۱) ایمیل استعلام عمده به wholesale@mtcgame.com و فرم Partner Alliance SEAGM و GIFQ؛ ۲) سؤال صریح انطباق: «Do you accept resellers based in Iran?»؛ ۳) تست پرداخت $50 با USDT TRC20 در Bitrefill؛ ۴) تکمیل قیمت‌های [نیازمند استعلام] در IRAN-MARKET-PRICING.md.
