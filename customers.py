"""
顧客管理モジュール
"""

customers = []

def add_customer(name, company, email, phone):
    """顧客を追加する"""
    customer = {
        "id": len(customers) + 1,
        "name": name,
        "company": company,
        "email": email,
        "phone": phone,
        "status": "active"
    }
    customers.append(customer)
    return customer

def get_customer(customer_id):
    """IDで顧客を取得する"""
    for customer in customers:
        if customer["id"] == customer_id:
            return customer
    return None

def list_customers():
    """全顧客を一覧表示する"""
    if not customers:
        print("顧客データがありません")
        return
    for c in customers:
        print(f"[{c['id']}] {c['name']} / {c['company']} / {c['email']}")

def update_status(customer_id, new_status):
    """顧客のステータスを更新する"""
    customer = get_customer(customer_id)
    if customer:
        customer["status"] = new_status
        return True
    return False
