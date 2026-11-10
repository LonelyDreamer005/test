## PART OF TEST BRANCH

'''
HI
'''

# cURL Commands

\# 1. Root route curl http://localhost:5000/  # 2. Get all students curl http://localhost:5000/students  # 3. Get student by ID curl http://localhost:5000/students/1  # 4. Create student curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{"name": "rahul", "course": "mech"}'  # 5. Update student curl -X PATCH http://localhost:5000/students/1 -H "Content-Type: application/json" -d '{"course": "ai/ml"}'  # 6. Delete student curl -X DELETE http://localhost:5000/students/2  # 7. Get all students (verify) curl http://localhost:5000/students