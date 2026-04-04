"""
商談管理モジュール
"""

deals = []

def add_deal(customer_id, title, amount, stage):
    """商談を追加する"""
    deal = {
        "id": len(deals) + 1,
        "customer_id": customer_id,
        "title": title,
        "amount": amount,
        "stage": stage  # prospect / negotiation / closed_won / closed_lost
    }
    deals.append(deal)
    return deal

def get_deals_by_customer(customer_id):
    """顧客IDで商談を取得する"""
    return [d for d in deals if d["customer_id"] == customer_id]

def get_total_amount():
    """成約済み商談の合計金額を計算する"""
    total = 0
    for deal in deals:
        if deal["stage"] == "closed_won":
            total = total + deal["amount"]
    return total

def list_deals():
    """全商談を一覧表示する"""
    if not deals:
        print("商談データがありません")
        return
    for d in deals:
        print(f"[{d['id']}] {d['title']} / ¥{d['amount']:,} / {d['stage']}")
