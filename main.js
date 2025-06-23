cl = s => console.log(s);

function factorial(num) {
    if (num === 0) {
        return 1
    }else {
        return num * factorial(num - 1)
    }

}

function fibonacci(n) {
    if (n === 0 || n === 1) {
        return n
    }else {
        return cl(fibonacci(n-1) + fibonacci(n-1))
    }
}

let a = factorial(4)
let b = fibonacci(5)
cl(b)