# Tekton

https://tekton.dev/

Works with the k8s resource model.
Resources are defined in yaml. Tekton catalog contains
reusable blocks. No need to invent the wheel. Everyone can contribute.
Scales with the cluster, this is probably handles by the scheduler.

Why no tekton?

- Existing pipelines, but bad excuse :shrug:
- k8s resource model, so when not running on kubernetes
- tekton is in early stages

Tekton Components

- Task:
  - Which steps are executed
  - `kind: Task`
  - spec with list of tasks, each task has a script. Looks like GH actions steps.
  - The task is a pod, each step is a container.
  - `kind: ClusterTask` is available in the entire cluster. Use case is centralized tasks which will be used by all teams
- Pipeline:
  - Series of tasks
  - `kind: Pipeline`
  - spec has a list of tasks, `taskRef.name` has reference to the task resource
  - orchestrate tasks, e.g. wait for other task, run in parallel
- TaskRuns and PipelineRuns
  - Instance of a `Task` or `Pipeline`
  - `spec.pipelineRef.name` is the reference to the Pipeline resource
  - `spec.params` passes values to the Pipeline.

Tekton on a container platform

Tekton and GitOps:
- Build pipeline is triggered after commit on repository:
    - Image is pushed to image registry
    - application version is pushed to gitops repository (tm-versions)
      - git commit happens, so tekton starts deployment pipeline
      - tekton applies changes from environment repository
- Works perfectly with ArgoCD
  - How does Argo work with kustomize?
  - Instead of letting Tekton apply the environment, just let ArgoCD watch it

Examples
- Basically the trendminer example. Create new namespace on PR. Use Kustomize with the target branch namespace.
  - Deploy all components from the e.g. master namespace, except the feature/test component
  - Make PR, create namespace, run integration tests, merge PR, delete namespace
- https://tekton.dev/docs/dashboard/
- Build base images with Tekton and https://knative.dev/docs/ eventing
  - Knative watches the `ImageStream` object on OpenShift, not sure how this works on plain k8s
  - https://docs.openshift.com/container-platform/4.6/openshift_images/image-streams-manage.html
  - Dockerfiles are templated by the Tekton pipeline using jinja2