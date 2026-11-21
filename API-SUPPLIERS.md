# API-SUPPLIERS — تأمین‌کنندگان دارای API (2026-11-21)

> فقط endpointهایی که در مستندات رسمی دیده شد ثبت شده‌اند؛ هیچ endpoint ساختگی‌ای وجود ندارد.

| تأمین‌کننده | وضعیت API | لینک مستندات | احراز هویت | Endpointهای مستندشده | Sandbox |
|---|---|---|---|---|---|
| SEAGM | عمومی و کامل | doc.openapi.seagm.io | HMAC-SHA256 | GET /v1/me (موجودی)؛ GET /v1/card-categories؛ GET /v1/card-types؛ POST /v1/card-orders؛ /v1/recharge-*؛ webhook؛ account-history | بله — openapi.seagm.io (تولید: openapi.seagm.com)؛ خرید با SEAGM Credits |
| Digiseller (Plati.market) | عمومی و کامل | my.digiseller.com/inside/api_general.asp | POST /api/apilogin با seller_id + timestamp + SHA256(API key+timestamp)؛ توکن 2 ساعته | GET /api/token/perms؛ GET /api/purchases/unique-code/{code}؛ PUT /api/purchases/unique-code/{code}/deliver؛ GET /api/purchase/info/{invoice_id}؛ GET /api/purchase/cart؛ legacy: agent_get.asp/agent_check.asp | Sandbox مستند نشد؛ Rate limit: 30 درخواست/دقیقه؛ Base: api.digiseller.com/api |
| G2G | مستند — فعال‌سازی مشروط | docs.g2g.com | API Key از پنل فروشنده | Offer management، Inventory، Create Offer / Upload Code / Order Delivery | شرط: Seller Level 30 |
| Kinguin | مستند — دسترسی روی درخواست | kinguin.net/dev-portal/documentation | API Key (ثبت‌نام dev portal) | Sales Manager API v1 (offers، stock، wholesale tier prices، reservations، alerts) + Envoy Webhooks؛ eCommerce API سمت خریدار | OpenAPI قابل دانلود در dev-portal |
| CoinGate GIFQ | مستند | docs.gifq.com/docs | API Key | REST + webhooks (سفارش کارت عمده) | بله — طبق docs |
| Bitrefill | مستند — Partner Program | docs.bitrefill.com/docs/api-overview | API Key (درخواست از /integrate) | Gift card catalog + buy، BRGC batches، invoice creation (POST /invoices)، affiliate | طبق docs؛ refund_address برای پرداخت کریپتو اجباری |
| Cryptorefills | عمومی بدون تأیید قبلی | cryptorefills.com/en/api-docs | توکن عمومی طبق docs | REST /v5/orders (عمومی)؛ Whitelabel /v6/partner/orders (revenue-share)؛ MCP server: api.cryptorefills.com/mcp/http | UNVERIFIED |
| MTCGame | خصوصی — روی درخواست | مستندات عمومی ندارد | — | مسیر درخواست: bizdev@mtcgame.com (B2B+API) و wholesale@mtcgame.com | — |
| OffGamers | خصوصی — برای شرکای Channel | مستندات عمومی ندارد | — | مسیر درخواست: reseller@offgamers.com (برنامه Channel با eKYC) | — |
| Xoxoday Plum | مستند enterprise | help-plum.xoxoday.com/api-reference/overview | API Key | GET vouchers، POST /v1/orders، webhook | sandbox دارد؛ KYB enterprise |

## تأمین‌کنندگان بدون API (روش عملیاتی مستند)

| تأمین‌کننده | روش سفارش/تحویل |
|---|---|
| Coinsbee | checkout وب + تحویل ایمیل فوری؛ بدون برنامه B2B یافت‌شده |
| Eneba/Gamivo/K4G/MMOGA/CDKeys | خرده‌فروشی وب؛ تحویل کد/ایمیل |
| FunPay/GGSel | خرید از مارکت‌پلیس با داوری داخلی؛ تحویل چت/کد |
| Eldorado.gg | خرید با TradeShield (escrow)؛ تحویل فوری پس از تأیید |
