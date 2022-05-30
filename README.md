
# Quality-Control



<!--- If we have only one group/collection, then no need for the "ungrouped" heading -->



## Endpoints

* [Auth](#auth)
    1. [Registro](#1-registro)
    1. [Login](#2-login)
    1. [Refresh](#3-refresh)
    1. [Logout (Revoke Access  token)](#4-logout-revoke-access--token)
    1. [Logout2 (Revoke Refresh token)](#5-logout2-revoke-refresh-token)
* [Device](#device)
    1. [Get Devices](#1-get-devices)
    1. [Get Devices By Id](#2-get-devices-by-id)
    1. [Create Device](#3-create-device)
    1. [Delete Device](#4-delete-device)
    1. [Edit Device](#5-edit-device)
* [Result](#result)
    1. [Get Results](#1-get-results)
    1. [Get Result By Id](#2-get-result-by-id)
    1. [Create Result](#3-create-result)
    1. [Delete Result](#4-delete-result)
* [Test](#test)
    1. [Get Tests](#1-get-tests)
    1. [Create Test](#2-create-test)
    1. [Edit Test](#3-edit-test)
    1. [Delete Test](#4-delete-test)
* [User](#user)
    1. [Get Users](#1-get-users)
    1. [Get Users By Id](#2-get-users-by-id)

--------



## Auth



### 1. Registro



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: https://qualitycontrol.herokuapp.com/api/v1/register
```



***Body:***

```js        
{
    "employee": {
        "emp_name": "Nome Empregado",
        "registry": "Mat123"
    },
    "login": "user",
    "password": "senha123",
    "user_role": 1
}
```



### 2. Login



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: https://qualitycontrol.herokuapp.com/api/v1/login
```



***Body:***

```js        
{
    "login": "user",
    "password": "senha123"
}
```



### 3. Refresh



***Endpoint:***

```bash
Method: POST
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/refresh
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2MDg4NCwianRpIjoiYjMxM2YzYzUtYTg4MC00MmU5LThlOTctZmM3YWI3Y2MyM2I5IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOnsidXNlcl9yb2xlIjoxLCJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIifSwibmJmIjoxNjUzODYwODg0LCJleHAiOjE2NTY0NTI4ODR9.VUP5cMLurRUohVU33cPny-k-JNoNqAeM2UPtSFXh4vkerK4RINBSZsRUVAQSfexfUiK0oCBttefFPcza3OAD-w |  |



### 4. Logout (Revoke Access  token)



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/logout
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2MDg4NCwianRpIjoiNjMzMTAwYzEtMDNjMy00N2I3LWJiMDAtNTE0N2ZlNmNhMDBhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsImlkX3VzZXIiOjMsImxvZ2luIjoidXNlciJ9LCJuYmYiOjE2NTM4NjA4ODQsImV4cCI6MTY1Mzg2MTI0NH0.UTfaLM6rhoOd4A_oSw_67-tl54DcUs8AKqXNM9n1NmwWe_O3AAI05U6fCzuGoggT_VhI5IoJAyfpKQDyKrSPqw |  |



### 5. Logout2 (Revoke Refresh token)



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/logout2
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2MDg4NCwianRpIjoiYjMxM2YzYzUtYTg4MC00MmU5LThlOTctZmM3YWI3Y2MyM2I5IiwidHlwZSI6InJlZnJlc2giLCJzdWIiOnsidXNlcl9yb2xlIjoxLCJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIifSwibmJmIjoxNjUzODYwODg0LCJleHAiOjE2NTY0NTI4ODR9.VUP5cMLurRUohVU33cPny-k-JNoNqAeM2UPtSFXh4vkerK4RINBSZsRUVAQSfexfUiK0oCBttefFPcza3OAD-w |  |



## Device



### 1. Get Devices



***Endpoint:***

```bash
Method: GET
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/devices
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2MjQxNSwianRpIjoiYzg4NDU0NWEtMzQwMi00NzRkLWJiMmMtNTI0OTE5OWU2Y2FmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsImlkX3VzZXIiOjMsImxvZ2luIjoidXNlciJ9LCJuYmYiOjE2NTM4NjI0MTUsImV4cCI6MTY1Mzg2Mjc3NX0.YA6KzJ8cspp85IT7XoE9P24AtGG1sUSDfLsdTKQ83fy0IAf_XIUN98k9GGoh9n1_UFFzyRaHiSRuDXpGhu9i0Q |  |



### 2. Get Devices By Id



***Endpoint:***

```bash
Method: GET
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/devices/1
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2NDM5OCwianRpIjoiZDc3ZGNiNjctZWJmMi00NjMyLTllZWItYTQ1MzY5NGNhZWY2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsImlkX3VzZXIiOjMsImxvZ2luIjoidXNlciJ9LCJuYmYiOjE2NTM4NjQzOTgsImV4cCI6MTY1Mzg2NDc1OH0.HCbtQB4LJIriPkaWpYxgRKJ68F2EwPLrJT21A5ytR3sHUAbejZ5BvJ4lUtvbeeUCA7GdLJrgUAIWnOifSxfLhw |  |



### 3. Create Device



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: https://qualitycontrol.herokuapp.com/api/v1/devices
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2NDM5OCwianRpIjoiZDc3ZGNiNjctZWJmMi00NjMyLTllZWItYTQ1MzY5NGNhZWY2IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsImlkX3VzZXIiOjMsImxvZ2luIjoidXNlciJ9LCJuYmYiOjE2NTM4NjQzOTgsImV4cCI6MTY1Mzg2NDc1OH0.HCbtQB4LJIriPkaWpYxgRKJ68F2EwPLrJT21A5ytR3sHUAbejZ5BvJ4lUtvbeeUCA7GdLJrgUAIWnOifSxfLhw |  |



***Body:***

```js        
{
    "brand": "BRAND TEST 3",
    "device_name": "DEVICE TEST 3",
    "model": "MODEL0012",
    "serie_number": "SN0701"
}
```



### 4. Delete Device



***Endpoint:***

```bash
Method: DELETE
Type: RAW
URL: https://qualitycontrol.herokuapp.com/api/v1/devices/2
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2MTk3OCwianRpIjoiMmI0N2U5MzktM2FhOC00YzE5LWEzMzQtZGViMzhmNDI2Y2I4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsImlkX3VzZXIiOjMsImxvZ2luIjoidXNlciJ9LCJuYmYiOjE2NTM4NjE5NzgsImV4cCI6MTY1Mzg2MjMzOH0.dQIPGqaiUtty9ux7fwglYqb0mfHtmCiVktP1-r5fpPRR2MafTxBauAXew6Urbde9mqKNnA8_CJP1JOqwpsAEig |  |



### 5. Edit Device



***Endpoint:***

```bash
Method: PUT
Type: RAW
URL: https://qualitycontrol.herokuapp.com/api/v1/devices/3
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2NDgyNCwianRpIjoiMWJjOGQ4ZjgtMDhhYi00ZjFiLWE2ZGYtMjM3OTUxZWRhMmI5IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJ1c2VyX3JvbGUiOjEsImlkX3VzZXIiOjMsImxvZ2luIjoidXNlciJ9LCJuYmYiOjE2NTM4NjQ4MjQsImV4cCI6MTY1Mzg2NTE4NH0.U0xjXBX5iB6s8HE-YyGl-dmnB3p7XyAj_2nMQ2Tx1_T1xh6eUX3BGsnBHSX75xnSzcd_kXKjzVnv64a4rJeyGA |  |



***Body:***

```js        
{
    "brand": "BRAND TEST 3 EDITED",
    "device_name": "DEVICE TEST 3 EDITED",
    "model": "MODEL0012",
    "serie_number": "SN0701"
}
```



## Result



### 1. Get Results



***Endpoint:***

```bash
Method: GET
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/results
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2NjI0MywianRpIjoiNGQwMjI1ZmYtMzQ1MS00YTkzLWEwMWMtOThmYTQ1NjczYzg1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4NjYyNDMsImV4cCI6MTY1Mzg2NjYwM30.LKWJ9XVpOOycxchN2UZ0MOCSTb-Hzr2AiwMHe6QPBufl8kxoLso1jJhmzSCdK7GxyRDVQRmK8AMqPAOBxIbJrg |  |



### 2. Get Result By Id



***Endpoint:***

```bash
Method: GET
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/results/1
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2NTY0OCwianRpIjoiZDJjZTg4NWYtZjMxNi00ZTIwLTk5NjQtOTQwY2Q3MjIyYmIyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4NjU2NDgsImV4cCI6MTY1Mzg2NjAwOH0.vBzkQb-Yu3mHZ4iHPJr7Z5VopnrhbjQLPsnwz2NyqaBudf8iSa4hsLHaZKihmr0WsIzgIBa6As4A5E4Emf1kaA |  |



### 3. Create Result



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: https://qualitycontrol.herokuapp.com/api/v1/results
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2NjI0MywianRpIjoiNGQwMjI1ZmYtMzQ1MS00YTkzLWEwMWMtOThmYTQ1NjczYzg1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4NjYyNDMsImV4cCI6MTY1Mzg2NjYwM30.LKWJ9XVpOOycxchN2UZ0MOCSTb-Hzr2AiwMHe6QPBufl8kxoLso1jJhmzSCdK7GxyRDVQRmK8AMqPAOBxIbJrg |  |



***Body:***

```js        
{
    "id_device": 1,
    "id_employee": 1,
    "measured_value": "1",
    "result_desc": "aprovado",
    "tests": [
        {
            "id_test": 8
        },
        {
            "id_test": 6
        }
    ]
}
```



### 4. Delete Result



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/results/3
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2NjI0MywianRpIjoiNGQwMjI1ZmYtMzQ1MS00YTkzLWEwMWMtOThmYTQ1NjczYzg1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4NjYyNDMsImV4cCI6MTY1Mzg2NjYwM30.LKWJ9XVpOOycxchN2UZ0MOCSTb-Hzr2AiwMHe6QPBufl8kxoLso1jJhmzSCdK7GxyRDVQRmK8AMqPAOBxIbJrg |  |



## Test



### 1. Get Tests



***Endpoint:***

```bash
Method: GET
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/tests
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2ODk5NiwianRpIjoiMzMyOTNmZGUtOGFiYi00OTc4LTkwZTYtNTJjMzYwYjU0M2MzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4Njg5OTYsImV4cCI6MTY1Mzg2OTM1Nn0.SVQETrQkFbOLsEmXeIsaNLEobAxuqrUtnOdVvW5gbtSnIUIsBJ1abf6zK8IKTk8S66a96YcUe6F_2zoAnY1cXw |  |



### 2. Create Test



***Endpoint:***

```bash
Method: POST
Type: RAW
URL: https://qualitycontrol.herokuapp.com/api/v1/tests
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2ODk5NiwianRpIjoiMzMyOTNmZGUtOGFiYi00OTc4LTkwZTYtNTJjMzYwYjU0M2MzIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4Njg5OTYsImV4cCI6MTY1Mzg2OTM1Nn0.SVQETrQkFbOLsEmXeIsaNLEobAxuqrUtnOdVvW5gbtSnIUIsBJ1abf6zK8IKTk8S66a96YcUe6F_2zoAnY1cXw |  |



***Body:***

```js        
{
    "id_test_type": 5,
    "max_value": null,
    "min_value": null,
    "test_name": "New Test"
}
```



### 3. Edit Test



***Endpoint:***

```bash
Method: PUT
Type: RAW
URL: https://qualitycontrol.herokuapp.com/api/v1/tests/56
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2OTU1MSwianRpIjoiNmZlMTUyZWUtMjZhZC00NWNkLWIwZmQtZWE4MzAwMzM2YmIyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4Njk1NTEsImV4cCI6MTY1Mzg2OTkxMX0.OtYnqBqAXCzfCJrh2YnxXNG4jCbnehIw7J7K4hxjt2TSKwgjKm_KR5UIaf0xLrbdLVMe6RJ48LmQXnlgSqp-EA |  |



***Body:***

```js        
{
    "id_test_type": 6,
    "max_value": null,
    "min_value": null,
    "test_name": "New Test Edited"
}
```



### 4. Delete Test



***Endpoint:***

```bash
Method: DELETE
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/tests/56
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2OTU1MSwianRpIjoiNmZlMTUyZWUtMjZhZC00NWNkLWIwZmQtZWE4MzAwMzM2YmIyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4Njk1NTEsImV4cCI6MTY1Mzg2OTkxMX0.OtYnqBqAXCzfCJrh2YnxXNG4jCbnehIw7J7K4hxjt2TSKwgjKm_KR5UIaf0xLrbdLVMe6RJ48LmQXnlgSqp-EA |  |



## User



### 1. Get Users



***Endpoint:***

```bash
Method: GET
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/users
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2OTU1MSwianRpIjoiNmZlMTUyZWUtMjZhZC00NWNkLWIwZmQtZWE4MzAwMzM2YmIyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4Njk1NTEsImV4cCI6MTY1Mzg2OTkxMX0.OtYnqBqAXCzfCJrh2YnxXNG4jCbnehIw7J7K4hxjt2TSKwgjKm_KR5UIaf0xLrbdLVMe6RJ48LmQXnlgSqp-EA |  |



### 2. Get Users By Id



***Endpoint:***

```bash
Method: GET
Type: 
URL: https://qualitycontrol.herokuapp.com/api/v1/users/1
```


***Headers:***

| Key | Value | Description |
| --- | ------|-------------|
| Authorization | Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1Mzg2OTk2NCwianRpIjoiNTI2NDk3ZmQtYzQ3My00ZDRiLTlhZDQtMDY2ZTc3M2MxZTA1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZF91c2VyIjozLCJsb2dpbiI6InVzZXIiLCJ1c2VyX3JvbGUiOjF9LCJuYmYiOjE2NTM4Njk5NjQsImV4cCI6MTY1Mzg3MDMyNH0.Vw2FU-PvrWw0b2jpoKUHGtimUE-qm3pt9IKbptYiddd_s6HCvQWGDS9cjW4I53jBJbKxzpkGezA0GDADopJLcg |  |



---
[Back to top](#quality-control)

>Generated at 2022-05-30 01:33:07 by [docgen](https://github.com/thedevsaddam/docgen)
