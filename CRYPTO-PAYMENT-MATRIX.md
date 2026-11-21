# CRYPTO-PAYMENT-MATRIX — ماتریس پرداخت رمزارزی (2026-11-21)

> منبع هر ردیف: پروفایل DOCX همان تأمین‌کننده + EVIDENCE. هیچ ادعایی بدون مدرک URL ثبت نشده است.

قاعده: پرداخت با کارت بانکی خارجی یا PayPal جایگزین پرداخت رمزارزی محسوب نمی‌شود و فقط به‌عنوان گزینه جایگزین ثبت می‌گردد.

| تأمین‌کننده | وضعیت | ارزها | شبکه USDT | حد/سقف | کارمزد | فاکتور | بازپرداخت رمزارزی | مدرک |
|---|---|---|---|---|---|---|---|---|
| Bitrefill | **VERIFIED** | BTC، Lightning، ETH، USDT، USDC، LTC، DOGE، Dash | انتخاب در Checkout [نیازمند استعلام] | [نیازمند استعلام] | کارمزد شبکه؛ بدون کارمزد محصول مشاهده‌شده | سوابق حساب؛ فاکتور رسمی [نیازمند استعلام] | [نیازمند استعلام] | docs.bitrefill.com/docs/api-overview + صفحات محصول |
| Coinsbee | **VERIFIED** | ۲۵۰+ کوین: USDT، USDC، BTC، ETH، SOL، LTC | **TRC-20 صریح** (متریال رسمی) | [نیازمند استعلام] | [نیازمند استعلام] | [نیازمند استعلام] | پس از تحویل معمولاً غیرممکن [تأییدشده با منبع] | coinsbee.com/en/gift-cards/games/playstation |
| GGSel | PARTIALLY VERIFIED | USDT (+ کارت روسی/Visa/MC/SBP) | [نیازمند استعلام] | [نیازمند استعلام] | [نیازمند استعلام] | سوابق درون‌پلتفرمی [نیازمند استعلام] | [نیازمند استعلام] | ggsel.net کاتالوگ PSN |
| FunPay | PARTIALLY VERIFIED | USDT TRC20 (+ کارت‌ها) | TRC20 | مبلغ دقیق طبق سند پرداخت | [نیازمند استعلام] | درون‌پلتفرمی [نیازمند استعلام] | [نیازمند استعلام] | سند USDT TRC20 FunPay |
| CodesWholesale | CONTACT REQUIRED | — | — | — | — | — | — | هیچ مدرکی یافت نشد |
| Oyunfor | CONTACT REQUIRED | — | — | — | — | — | — | فقط پرداخت TRY مشاهده شد |
| Kinguin | UNKNOWN | — | — | — | — | — | — | بررسی نشد |
| Plati.market / Digiseller | UNKNOWN | پنل: USD/RUB/EUR/UAH | — | — | — | — | — | plati.market |
| Reloadly / Tillo / Xoxoday | UNKNOWN (بدون اشاره رمزارز در متریال) | — | — | — | — | — | — | سایت‌های رسمی |
| OneCard / Bitaqaty | UNKNOWN | — | — | — | — | — | — | v2docs.onecard.com |

## به‌روزرسانی S01 — ردیف‌های تأییدشده مستقیم (2026-11-21)

| تأمین‌کننده | وضعیت | ارزها | شبکه USDT | حد/سقف | کارمزد | فاکتور | بازپرداخت رمزارزی | مدرک |
|---|---|---|---|---|---|---|---|---|
| Cryptorefills | **VERIFIED** | USDT، USDC، ETH، BTC، LTC، DOGE و 20+ دارایی | **Tron (TRC20) صریح** در تسویه API («USDT on Tron») | بدون prefunding؛ per-order | تسویه استیبل‌کوین؛ جزئیات کارمزد [نیازمند استعلام] | جریان API (price→validate→order→track) | [نیازمند استعلام] | cryptorefills.com/en/insights/gift-card-api-fintech-rewards-platforms |
| CoinGate GIFQ | PARTIALLY VERIFIED | BTC، ETH، USDC، LTC، BCH، DOGE، XRP، SOL، ADA، TRON، BNB، DAI و 65+ — **USDT در فهرست مشاهده نشد** | [نیازمند استعلام] | «from ten cards to ten thousand» | «Crypto checkouts carry 0% fees» | فاکتور تجاری واحد | سفارش ناموفق بازگشت وجه دارد [تأییدشده با منبع] | coingate.com/gift-cards |
| SEAGM | **VERIFIED** | BTC، ETH، USDT (5 گزینه رمزارزی) | نامشخص — درگاه TripleA | [نیازمند استعلام] | TripleA | رسید درگاه | **بدون بازگشت وجه رمزارزی (irrevocable)** [تأییدشده با منبع] | help.seagm.com/hc/en/articles/1352 |
| OffGamers | **VERIFIED** | BTC، USDT-ETH، USDT-Polygon، Crypto.com | **ERC20 و Polygon صریح** | [نیازمند استعلام] | [نیازمند استعلام] | رسید درگاه | لغو فقط به‌صورت اعتبار فروشگاه [تأییدشده با منبع] | payment-guide.offgamers.com/payment-guide/pg/cryptocurrency/bitcoin |
| Gamivo | PARTIALLY VERIFIED | BTC، BCH، ETH، USDT (از Q4 2022) | [نیازمند استعلام] | [نیازمند استعلام] | [نیازمند استعلام] | رسید پرداخت | [نیازمند استعلام] | بیانیه رسمی gamivo.co (منبع 2022 — وضعیت فعلی باید تست شود) |
| Kinguin | NOT SUPPORTED (مستقیم) | — رمزارز فقط به‌عنوان محصول (کارت ووچر) | — | — | — | — | مسیر غیرمستقیم: گیفت‌کارت Kinguin از Bitrefill با USDT/BTC/LTC | صفحات Kinguin + bitrefill.com |
| MTCGAME | CONTACT REQUIRED | سند تاریخی BTC با TripleA؛ وضعیت فعلی نامشخص؛ روش فعلی کارت/Stripe | UNKNOWN | [نیازمند استعلام] | [نیازمند استعلام] | [نیازمند استعلام] | [نیازمند استعلام] | mtcgame.com/page/partnership + سند S02 |
| Turgame B2B | UNKNOWN | هیچ روش پرداختی منتشر نشده | — | — | — | — | — | wholesale.turgame.com |
