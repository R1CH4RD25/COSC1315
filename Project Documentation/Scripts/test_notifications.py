"""
Test Notification Script
Generates system notifications on Windows without requiring specific hardware
"""

from plyer import notification
import time

def send_test_notification(title="Test Notification", message="This is a test message", timeout=10):
    """
    Send a system notification
    
    Args:
        title: Notification title
        message: Notification message
        timeout: How long notification displays (seconds)
    """
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="COSC1315 Test",
            timeout=timeout
        )
        print(f"✅ Notification sent: {title}")
    except Exception as e:
        print(f"❌ Error sending notification: {e}")

if __name__ == "__main__":
    print("Testing notifications...")
    
    # Test 1: Simple notification
    send_test_notification(
        title="Hello from COSC1315",
        message="This is a test notification!",
        timeout=5
    )
    
    time.sleep(2)
    
    # Test 2: Assignment reminder
    send_test_notification(
        title="Assignment Due Soon",
        message="Lesson 03: Variables is due in 24 hours",
        timeout=10
    )
    
    print("\nNotification tests complete!")
