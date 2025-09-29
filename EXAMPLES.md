# Examples

## Python
```python
from duruzi.client import DuruziClient
c = DuruziClient("http://localhost:8080", api_key="sk_test")
print(c.infer("demo", "Hello Duruzi"))
```

## JavaScript
```js
import { infer } from 'duruzi-sdk'
const res = await infer("http://localhost:8080", "sk_test", "demo", "Hello Duruzi")
console.log(res)
```
