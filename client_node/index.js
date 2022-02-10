const Express = require("express");
const bodyParser = require("body-parser");
const logger = require("morgan");
const app = Express();

app.use(bodyParser({extended: true}));
app.use(logger("dev"));

const grpc = require("@grpc/grpc-js");
const protoLoader = require("@grpc/proto-loader");
const path = require("path");

const protoObject = protoLoader.loadSync(path.resolve(__dirname, "../proto/TaskList.proto"));
const TaskListDefinition = grpc.loadPackageDefinition(protoObject);
const client = new TaskListDefinition.TaskListPackage.TaskList("0.0.0.0:50051", grpc.credentials.createInsecure());

app.post("/createTask", (req, res) => {
    client.createTask({title: req.body["title"], description: req.body["description"]}, (err, response) => {
        if (!err)
            return res.status(500).end();
        return res.status(201).json(response);
    });
});

app.get("/listTasks", (req, res) => {
    client.listTasks({}, (err, response) => {
        if (!err)
            return res.status(500).end();
       return res.status(200).json(response);
    });
});

app.put("/complete/:id", (req, res) => {
   client.completeTask({ id: req.params["id"] }, (err) => {
       if (!err)
           return res.status(500).end();
       return res.status(200).end();
   });
});

app.listen(3000, () => {
    console.log("Server started @ http://0.0.0.0:3000");
});