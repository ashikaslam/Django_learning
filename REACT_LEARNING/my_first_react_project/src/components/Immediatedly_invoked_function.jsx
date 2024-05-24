

const  my_murk=75;

const Immediatedly_invoked_function = () => {
    return (
        <div>
            
{(

()=>{
if(my_murk>80){
    return<h1>A+</h1>
}
else if(my_murk>70){
    return<h1>A+</h1>
}
else if(my_murk>60){
    return <h1>A-</h1>
}
else if(my_murk>50){
    return <h1>B</h1>
}
else if(my_murk>40){
    return<h1>B-</h1>
}
else if(my_murk>32){
    return <h1>C</h1>
}
else{
    return<h1>F</h1>
}

}

)()}



        </div>
    );
};

export default Immediatedly_invoked_function;