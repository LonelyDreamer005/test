## PART OF TEST BRANCH

'''
HI
'''

# cURL Commands

\# 1. Root route curl http://localhost:5000/  # 2. Get all students curl http://localhost:5000/students  # 3. Get student by ID curl http://localhost:5000/students/1  # 4. Create student curl -X POST http://localhost:5000/students -H "Content-Type: application/json" -d '{"name": "rahul", "course": "mech"}'  # 5. Update student curl -X PATCH http://localhost:5000/students/1 -H "Content-Type: application/json" -d '{"course": "ai/ml"}'  # 6. Delete student curl -X DELETE http://localhost:5000/students/2  # 7. Get all students (verify) curl http://localhost:5000/students

# kuber

\# 1. Start Minikube cluster
minikube start

\# 2. Load local Docker image into Minikube
minikube image load test-web:latest

\# 3. Apply Kubernetes manifests
kubectl apply -f k8s/

\# 4. Check status of resources
kubectl get pods
kubectl get deployment
kubectl get service

\# 5. Scale deployment to 3 replicas
kubectl scale deployment devops-app --replicas=3

\# 6. Verify scaled pods
kubectl get pods

\# 7. Get application URL
minikube service devops-service --url