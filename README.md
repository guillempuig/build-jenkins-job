# Build jenkins job from Github Action :rocket:

This action builds/triggers a jenkins job, waiting it to be finished and enabling to pass job params.

## Inputs

### `jenkins-token`

**Required**
 
 ### `jenkins-url`

**Required** 

### `jenkins-user`

**Required** 

### `job-path`

**Required** 

### `job-params`

**Not mandatory**

Set jenkins params as JSON string:
i.e 
```
 "{'param1': 'value1', 'param2': 'value2'}"
``` 


## Outputs

###  `status/result`

* FAILURE
* SUCCESS
* ABORTED


## Example usage
```
    - name: "Trigger jenkins job"
      uses: ./.github/actions/jenkins # Uses an action in the root directory
      with:
        jenkins-url: ${{ secrets.JENKINS_URL }}
        jenkins-token: ${{ secrets.JENKINS_TOKEN }}
        user: "jenkins-username"
        job-path: "/job/Fluid/job/fluid-controller-deploy"
        job-params: "{'param1': 'value1', 'param2': 'value2'}"
    - name: Get job status
      run: echo "Job status is ${{ steps.job-build.outputs.job_status }}"
``
