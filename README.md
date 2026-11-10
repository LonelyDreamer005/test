# DevOps Practical – Test Branch

## 1. Python Flask Application – cURL Commands

Start the Flask application:

```bash
python app.py
```

### 1.1 Check Application Status
```bash
curl http://localhost:5000/
```

### 1.2 Get All Students
```bash
curl http://localhost:5000/students
```

### 1.3 Get Student by ID
```bash
curl http://localhost:5000/students/1
```

### 1.4 Add a Student (POST)
```bash
curl -X POST http://localhost:5000/students \
-H "Content-Type: application/json" \
-d '{"name": "rahul", "course": "mech"}'
```

### 1.5 Update Student (PATCH)
```bash
curl -X PATCH http://localhost:5000/students/1 \
-H "Content-Type: application/json" \
-d '{"course": "ai/ml"}'
```

### 1.6 Delete a Student (DELETE)
```bash
curl -X DELETE http://localhost:5000/students/2
```

### 1.7 Verify Student Records
```bash
curl http://localhost:5000/students
```

---

## 2. Docker – Build and Run Container

### 2.1 Build Docker Image
```bash
docker build -t test-web:latest .
```

### 2.2 List Docker Images
```bash
docker images
```

### 2.3 Run Docker Container
```bash
docker run -d -p 5000:5000 --name test-container test-web:latest
```

### 2.4 Check Running Containers
```bash
docker ps
```

### 2.5 Test Application
```bash
curl http://localhost:5000/
```

### 2.6 Stop and Remove Container
```bash
docker stop test-container
docker rm test-container
```

---

## 3. Kubernetes – Deployment and Service

### 3.1 Start Minikube
```bash
minikube start
```

### 3.2 Load Docker Image into Minikube
```bash
minikube image load test-web:latest
```

### 3.3 Apply Kubernetes YAML Files
```bash
kubectl apply -f k8s/
```

### 3.4 Check Kubernetes Resources
```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

### 3.5 Get Application URL
```bash
minikube service devops-service --url
```

---

## 4. Kubernetes – Scaling

### 4.1 Scale to 2 Replicas
```bash
kubectl scale deployment devops-app --replicas=2
```

### 4.2 Verify Pods
```bash
kubectl get pods
```

### 4.3 Scale to 5 Replicas
```bash
kubectl scale deployment devops-app --replicas=5
```

### 4.4 Verify Deployment
```bash
kubectl get pods
kubectl get deployment
```

---

## 5. Kubernetes – Rolling Updates

### 5.1 Update Docker Image

Build and load `test-web:v2` into Minikube before updating:

```bash
docker build -t test-web:v2 .
minikube image load test-web:v2
```

### 5.2 Update Deployment
```bash
kubectl set image deployment/devops-app \
devops-container=test-web:v2
```

### 5.3 Check Update Status
```bash
kubectl rollout status deployment/devops-app
```

### 5.4 Check Rollout History
```bash
kubectl rollout history deployment/devops-app
```

### 5.5 Rollback Deployment
```bash
kubectl rollout undo deployment/devops-app
```

---

## 6. Kubernetes – ConfigMap

### 6.1 Apply ConfigMap
```bash
kubectl apply -f k8s/configmap.yaml
```

### 6.2 List ConfigMaps
```bash
kubectl get configmaps
```

### 6.3 Describe ConfigMap
```bash
kubectl describe configmap app-config
```

---

## 7. Terraform – Installation in Google Cloud Shell

### 7.1 Create Installation Directory
```bash
mkdir -p ~/bin
```

### 7.2 Add Terraform to PATH
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### 7.3 Download Terraform
```bash
cd /tmp

wget https://releases.hashicorp.com/terraform/1.7.5/terraform_1.7.5_linux_amd64.zip
```

### 7.4 Extract and Install
```bash
unzip terraform_1.7.5_linux_amd64.zip
mv terraform ~/bin/
```

### 7.5 Verify Installation
```bash
terraform version
```

---

## 8. Terraform – Infrastructure as Code

Navigate to the Terraform configuration directory:

```bash
cd ~/test/ter
```

### 8.1 Initialize Terraform
```bash
terraform init
```

### 8.2 Validate Configuration
```bash
terraform validate
```

### 8.3 Generate Execution Plan
```bash
terraform plan
```

### 8.4 Apply Infrastructure
```bash
terraform apply -auto-approve
```

### 8.5 Verify Created File
```bash
cat hello.txt
```

### 8.6 Inspect Infrastructure
```bash
terraform show
```

### 8.7 Destroy Infrastructure
```bash
terraform destroy -auto-approve
```

---

## 9. Git and GitHub – Basic Commands

### 9.1 Initialize Git
```bash
git init
```

### 9.2 Check Repository Status
```bash
git status
```

### 9.3 Stage Files
```bash
git add .
```

### 9.4 Commit Changes
```bash
git commit -m "Updated DevOps practical"
```

### 9.5 Push Changes to GitHub
```bash
git push origin main
```

### 9.6 Pull Latest Changes
```bash
git pull origin main
```

---

**End of DevOps Practical Commands**