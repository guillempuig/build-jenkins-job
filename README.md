# Hello world docker action

This action prints "Hello World" or "Hello" + the name of a person to greet to the log.

## Inputs

### `jenkins-token`

**Required**
 
 ### `jenkins-url`

**Required** 

### `jenkins-user`

**Required** 

### `job_path`

**Required** 

## Outputs

### `status"


## Example usage
```
    uses: ./.github/actions/jenkins # Uses an action in the root directory
    with:
      jenkins-url: ${{ secrets.JENKINS_URL }}
      jenkins-token: ${{ secrets.JENKINS_TOKEN }}
      user: "devops-qa"
      job-path: '/job/Fluid/job/fluid-controller-deploy'
``