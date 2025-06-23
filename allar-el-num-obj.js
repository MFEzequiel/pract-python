
let list = [9, 4, 10, 3, 39, 12, 1, 7, 6]


function towSum(array,target) {

    const differences = {};

    for (let i=0;i < array.length; i++){

        const n = array[i];
        
        if (differences[target - n]){

            return [differences[target - n].index, i]
        }

        differences[n] = {

            value: target - n,
            index: i

        }
    }
    return [];
}

let a = towSum(list, 5)
console.log(a)