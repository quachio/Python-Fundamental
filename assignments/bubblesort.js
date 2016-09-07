/**
 * Created by quachio on 9/6/16.
 */
console.log('Hello');

var arr = [5, 3, 2, 1];


for(var i = 0; i < arr.length; i++) {
    for(var k = 0; k < arr.length; k++) {
        if(arr[k] > arr[k+1]){
            var temp = arr[k];
            arr[k] = arr[k+1];
            arr[k+1] = temp;
        }
    }
    console.log(arr);
}

