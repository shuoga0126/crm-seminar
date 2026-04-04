"""
営業チームCRM - メインファイル

【セミナー用】このファイルにはバグが2つ仕込まれています。
/review コマンドで発見・修正してみましょう。
"""

from customers import add_customer, list_customers, get_customer
from sales import add_deal, list_deals, get_total_amount


def setup_demo_data():
    """デモ用のサンプルデータを追加する"""
    # 顧客を追加
    add_customer("田中 太郎", "株式会社ABC", "tanaka@abc.co.jp", "03-1234-5678")
    add_customer("鈴木 花子", "XYZ商事", "suzuki@xyz.co.jp", "03-8765-4321")
    add_customer("佐藤 次郎", "DEF工業", "sato@def.co.jp", "06-1111-2222")

    # 商談を追加
    add_deal(1, "基幹システム導入", 5000000, "negotiation")
    add_deal(1, "保守契約", 1200000, "closed_won")
    add_deal(2, "クラウド移行支援", 3000000, "closed_won")
    add_deal(3, "新規開発", 8000000, "prospect")


def show_summary():
    """サマリーを表示する"""
    print("=" * 40)
    print("営業チームCRM - サマリー")
    print("=" * 40)

    print("\n【顧客一覧】")
    list_customers()

    print("\n【商談一覧】")
    list_deals()

    # バグ①: 文字列と数値を + で結合しようとしている
    total = get_total_amount()
    print("\n【成約合計金額】")
    print("合計: ¥" + total)


def search_customer(keyword):
    """顧客名で検索する（バグ②: 比較方法が間違っている）"""
    results = []
    for i in range(1, len(results)):  # バグ②: results ではなく customers を参照すべき
        from customers import customers
        c = customers[i]
        if keyword in c["name"]:
            results.append(c)
    return results


if __name__ == "__main__":
    setup_demo_data()
    show_summary()
