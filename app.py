print("vithu")

user_feedback = ['service is good','excellent service','average srvices','just good']

user_feedback.append("it's excellent")## append method

positive_user_feedback = sum(1 for comment in user_feedback if 'good' in comment.lower() or 'excellent' in comment.lower() )
print(f"the feedback is : {positive_user_feedback}")

print("\n User Feedback : ")
for comment in user_feedback:
    print("-",comment)