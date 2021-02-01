// 'Hey World' nodejs12.x runtime AWS Lambda function
exports.handler = (event, context, callback) => {
    console.log('Hey, logs');
    callback(null, 'Successesfully created');
}
