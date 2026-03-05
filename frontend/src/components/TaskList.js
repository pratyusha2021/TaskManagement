import React,{useEffect,useState} from "react";
import API from "../api";

function TaskList(){

const [tasks,setTasks]=useState([]);

useEffect(()=>{

API.get("tasks/",{
headers:{
Authorization:
`Bearer ${localStorage.getItem("token")}`
}
})
.then(res=>setTasks(res.data));

},[]);

return(

<div>
<h2>Tasks</h2>

{tasks.map(task=>(
<p key={task.id}>{task.title}</p>
))}

</div>

)

}

export default TaskList;