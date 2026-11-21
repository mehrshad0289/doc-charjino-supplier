# API-SUPPLIERS — تأمین‌کنندگان دارای API (2026-11-21)

قانون: هیچ endpoint فرضی یا قابلیت تأییدنشده‌ای ثبت نمی‌شود؛ API خصوصی = روش درخواست دسترسی مستند می‌گردد.

| تأمین‌کننده | وضعیت API | لینک مستندات | احراز هویت | قابلیت‌های تأییدشده | Sandbox |
|---|---|---|---|---|---|
| Bitrefill | دارد — عمومی | docs.bitrefill.com/docs/api-overview | [نیازمند استعلام - جزئیات هدر/کلید] | Catalog + Purchase + Bulk Issuance + Balance (crypto deposit) [تأییدشده با منبع]؛ Webhook/Refund/Rate Limit [نیازمند استعلام] | [نیازمند استعلام] |
| CodesWholesale | دارد — پس از ثبت‌نام خریدار | [نیازمند استعلام] | [نیازمند استعلام] | «automate delivery with the API» + «zero inventory risk» [مشاهده‌شده در وب‌سایت] | [نیازمند استعلام] |
| Kinguin | دارد — Digital Wholesale Partnership | kinguin.net/integration (فرم) | [نیازمند استعلام] | معرفی عمومی API؛ جزئیات پس از پذیرش | [نیازمند استعلام] |
| Eneba | دارد — برای فروشندگان | eneba.com/sell-with-eneba | [نیازمند استعلام] | API integration فروشندگان [مشاهده‌شده در وب‌سایت] | [نیازمند استعلام] |
| GAMIVO | دارد — اتصال فروشگاه | gamivo.com/start-selling | [نیازمند استعلام] | «Connect your shop with GAMIVO via API» [مشاهده‌شده در وب‌سایت] | [نیازمند استعلام] |
| Digiseller (پشتوانه Plati) | دارد — عمومی برای فروشندگان | api.digiseller.com (XML API) | API Key پس از ثبت‌نام [مشاهده‌شده در وب‌سایت] | Seller goods، کاتالوگ، تحویل خودکار؛ کارمزد پلتفرم ~۱۰٪ [مشاهده‌شده در وب] | — |
| OneCard / Bitaqaty | دارد — Reseller Integration v2 | v2docs.onecard.com | [نیازمند استعلام] | تراکنش‌های Reseller [مشاهده‌شده در وب‌سایت] | — |
| Reloadly | دارد — عمومی | docs.reloadly.com | OAuth/Token [مشاهده‌شده در وب‌سایت] | Get Products و Gift Card API کامل [تأییدشده با منبع] | — |
| Tillo | دارد — B2B | tillo.com/gift-card-api | [نیازمند استعلام] | ۵٬۰۰۰+ برند، ۴۱ کشور [مشاهده‌شده در وب‌سایت]؛ نگرانی ممنوعیت resale | — |
| Oyunfor | درخواستی — «Oyunfor API Başvuru» | [نیازمند استعلام] | [نیازمند استعلام] | وجود گزینه درخواست API در منو [مشاهده‌شده در وب‌سایت] | — |
| Coinsbee / GGSel / FunPay | مستند نشد | — | — | عملیات پنلی | — |

## به‌روزرسانی S01 — تأیید مستقیم مستندات (2026-11-21)

| تأمین‌کننده | وضعیت API | احراز هویت (تأیید مستقیم) | قابلیت‌های تأییدشده | Sandbox |
|---|---|---|---|---|
| Bitrefill | دارد — سه سطح Personal/Business/Affiliate | Personal: Bearer token؛ Business/Affiliate: Basic auth base64(API_ID:API_SECRET) — Business نیازمند پذیرش Partner Program | پرداخت فاکتور با BTC/Lightning/ETH/USDC/USDT یا موجودی؛ Webhooks همه سطوح؛ BRGC batch؛ کاتالوگ 170+ کشور | Sandbox مستقل ندارد؛ محصولات تستی در سطح Business |
| Cryptorefills | دارد — REST v4/v5 + webhooks + MCP | جزئیات auth نیازمند استعلام | Endpoints تأییدشده: /v2/brands، /v5/products/country، /v4/products/price، /v5/orders/validations، /v5/orders؛ تسویه per-order با USDT-Tron/USDC-Solana؛ بدون KYC و بدون prefunding | نیازمند استعلام |
| CoinGate GIFQ | دارد — REST + webhooks | نیازمند استعلام (docs.gifq.com در فچ مستقیم 429 داد) | «REST API and webhooks to automate ordering, with sandbox access first»؛ volume pricing 10→10000 کارت | دارد (اعلامی) |
| Kinguin | دارد — Purchase API (ESA) برای خریدار | دسترسی با درخواست از dev-portal/api-access | راهنمای رسمی ESA + quickstart GitHub؛ قیمت Wholesale tier در API | نیازمند استعلام |
| Gamivo | فقط Seller API | نیازمند استعلام | «Connect your shop with GAMIVO via API»؛ Buyer API ندارد | — |
| Turgame B2B | ادعای JSON API (stock realtime، سفارش/تحویل خودکار) | نیازمند استعلام | ادعا بدون مستندات عمومی — قابل اثبات نیست | — |
| MTCGAME | API عمومی ندارد؛ تأیید کد «verified via API before delivery»؛ ادغام برای Reseller با درخواست | — | کانال رسمی Sony — عمده فقط با استعلام | — |
| SEAGM / OffGamers | ندارد | — | سفارش دستی؛ OffGamers: reseller@offgamers.com | — |
