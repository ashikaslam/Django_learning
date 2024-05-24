



const check=(flag)=>{

if (flag===true)return <button>logout</button>
else return <button>login</button>


/*2: switch 

switch (flag) {
    case true:
       return <button>logout</button>
    case false:
       return <button>logout</button>
    default:
        return <button>it is a default and it not comblsary</button>
}
*/


};





const yes_loign = false;
const Conditional_rendering = () => {
    return (
        <div>
            <h1>login status</h1>
                   {check(yes_loign)}


        </div>
    );
};

export default Conditional_rendering;