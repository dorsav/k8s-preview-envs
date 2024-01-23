# k8s-preview-envs
Deployment and destruction of preview envs based on PR status 

# myapp

This repository contains the configuration and deployment setup for managing preview environments of a sample Flask app using Kubernetes, Helm, and Kustomize.

- `app/`: Contains the files for the really dummy flask application
- `helm/`: Helm chart for managing Kubernetes deployment, holding both deployment and service yaml files and also base kustomization.yaml.
- `kustomize/`: Kustomize overlays for customizing dynamic preview envs, those kustomization.yaml files can override any *base* configuration, allowing differentiation of each env.

## Helm Chart - myapp

### Chart Structure

- `Chart.yaml`: Helm chart metadata.
- `values.yaml`: Default values for Helm chart.
- `templates/`: Kubernetes manifests for Deployment and Service.


## Kustomize Overlays

Kustomize is used here to customize Helm values based on the PR name

- `kustomize/overlays/preview/kustomization.yaml`: Kustomization file for the "preview" environment. (preview dir here is an example of an adhoc environment, env name is branch name)
- Each new env with will be described by a sub-directory under overlays directory, though will be present on the deployment time only, and will not be a part of the repo files. 

## Deployment Workflow
Triggered by a PR creation into main branch. 

1. Build and push the Docker image of the flask app to dorsav/myapp dockerhub registry, image tag will be same as branch name, so as k8s namespace.
2. Install the Helm chart using Kustomize for the desired environment, each overlay will override the base kustomization.yaml, and will basically use each deployment and service yamls with a changed image and namespace.
Everntually will run - 
   ```bash
   kubectl apply -k kustomize/overlays/<branch-name> -n <branch_name> 

## Access the deployed application in the specified namespace  
Go to Workloads page in GKE console and find your app, then at the botton of the page there will be a link to its NLB with port - 5000. That's the URL of the current Schwifty app.


## Destroying Preview Environments
Delete the corresponding Kubernetes namespace. Will run the PR is closed or merged. 

   ```bash
      kubectl delete -n <PR-name>
