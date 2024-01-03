class NotificationManager:

    def create_notification_content(self, event_data):
        # トリガーイベントに基づいて通知内容を作成
        # この関数は、イベントのデータを受け取り、通知の内容を準備します。
        title = "新しいイベントがあります"
        message = "詳細はこちら：{}".format(event_data)
        # 通知内容の辞書を返します
        return {"title": title, "message": message}

    def send_notification(self, notification_content, user):
        # 通知をユーザーに送信するための実装
        # ここでは例として、端的なプリント関数で代用していますが、
        # 実際にはメールサーバーを使ったり、プッシュ通知APIを呼び出したりします。
        print(f"Sending notification to {user}: {notification_content}")

# 他のファイルからこのクラスを利用して通知を送る例
def event_handler(event):
    # イベントが発生したときに呼ばれる処理を記述します。
    notification_manager = NotificationManager()
    notification_content = notification_manager.create_notification_content(event)
    users = ["user1@example.com", "user2@example.com"]  # 通知を送るユーザーのリスト
    for user in users:
        notification_manager.send_notification(notification_content, user)
