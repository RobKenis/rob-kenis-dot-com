const AWS = require('aws-sdk');
const ssm = new AWS.SSM();

const getParameter = async (name) => await ssm.getParameter({Name: name, WithDecryption: false}).promise()

exports.handler = async function (event, context) {
    const accountId = event.requestContext.accountId;

    const {Parameter: accessKey} = await getParameter('/workshop/guest/accesskey');
    const {Parameter: secretKey} = await getParameter('/workshop/guest/secretkey');
    const {Parameter: password} = await getParameter('/workshop/guest/password');

    return {
        statusCode: 200,
        headers: {
            "Access-Control-Allow-Origin" : "*", // Required for CORS support to work
            "Access-Control-Allow-Credentials" : true // Required for cookies, authorization headers with HTTPS
        },
        body: JSON.stringify({
            accessKey: accessKey.Value,
            secretKey: secretKey.Value,
            user: 'guest',
            password: password.Value,
            loginUrl: `https://${accountId}.signin.aws.amazon.com/console`
        }),
    }
}
