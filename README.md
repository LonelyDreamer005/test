# Part of Test Branch

```text
HI
```

---

# cURL Commands

Use the following commands to test the Flask Student API.

### 1. Check Root Route
```bash
curl http://localhost:5000/
```

### 2. Get All Students
```bash
curl http://localhost:5000/students
```

### 3. Get Student by ID
```bash
curl http://localhost:5000/students/1
```

### 4. Create a Student (POST)
```bash
curl -X POST http://localhost:5000/students \
-H "Content-Type: application/json" \
-d '{"name": "rahul", "course": "mech"}'
```

### 5. Update Student Details (PATCH)
```bash
curl -X PATCH http://localhost:5000/students/1 \
-H "Content-Type: application/json" \
-d '{"course": "ai/ml"}'
```

### 6. Delete a Student (DELETE)
```bash
curl -X DELETE http://localhost:5000/students/2
```

### 7. Verify Student Records
```bash
curl http://localhost:5000/students
```

---

# Kubernetes Commands

### 1. Start Minikube Cluster
```bash
minikube start
```

### 2. Load Local Docker Image into Minikube
```bash
minikube image load test-web:latest
```

### 3. Apply Kubernetes Manifests
```bash
kubectl apply -f k8s/
```

### 4. Check Resource Status
```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

### 5. Scale Deployment to 3 Replicas
```bash
kubectl scale deployment devops-app --replicas=3
```

### 6. Verify Scaled Pods
```bash
kubectl get pods
```

### 7. Get Application URL
```bash
minikube service devops-service --url
```
mkdir -p ~/bin
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
cd /tmp
wget https://releases.hashicorp.com/terraform/1.7.5/terraform_1.7.5_linux_amd64.zip
unzip terraform_1.7.5_linux_amd64.zip
mv terraform ~/bin/
cd ~/test
terraform init
terraform plan
terraform apply -auto-approve
cat hello.txt