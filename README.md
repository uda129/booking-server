# booking-server
這是一個簡單的訂單格單格式檢查與轉換的API
以docker包裝環境
並附有pytest進行覆蓋成功與失敗的案例

## SOLID原則
### 單一職責原則 SRP(A class should have only one reason to change)
將檢查與轉換中的任務拆分為3個processor, 分別對應處理name, price, currency的相關任務

### 開放封閉原則 OCP(Open–closed principle)
方便擴展, 未來想增加address功能, 可以開新的processor
亦不會影響到既有processor

### 里氏替換原則 LSP(Liskov substitution principle)
nameprocessor, priceprocessor, currencyprocessor繼承processor
子class擁有不同功能細別功能, 但皆有process這個功能需要實作

### 介面隔離原則 ISP(Interface segregation principle)
nameprocessor, priceprocessor, currencyprocessor各有其功能, 其細部功能不影響彼此

