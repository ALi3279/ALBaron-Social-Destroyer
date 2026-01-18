print("ALBaron Social Media Destroyer v1.0")
print("="*40)

password = input("Password: ")
if password == "ALBaron¥":
    target = input("Target username: ")
    
    print(f"\nAttacking: {target}")
    for i in range(10):
        print(f"Progress: {i+1}/10")
        import time
        time.sleep(0.3)
    
    print("\n" + "="*40)
    print("✅ تم النيك من قبل ALBaron")
    print(f"🎯 Target: {target}")
    print("💀 Account will be deleted")
    print("="*40)
else:
    print("Wrong password!")
