## build with buildpack and push
```sh

export DOCKER_USER=arllanos

pack build --builder=heroku/buildpacks:20 ${DOCKER_USER}/custom-model:v1

 docker push ${DOCKER_USER}/custom-model:v1

```
## deploy inference
```sh
cat << EOF > custom.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: custom-model
spec:
  predictor:
    containers:
      - name: kserve-container
        image: ${DOCKER_USER}/custom-model:v1
EOF

kubectl apply -f custom.yaml
```