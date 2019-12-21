function partition(arr, low, high) {
  let pivot = arr[high].avg;
  let i = low - 1;

  for (let j = low; j < high; j++) {
    if (arr[j].avg < pivot) {
      i++;

      let temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    }
  }

  let temp = arr[i + 1];
  arr[i + 1] = arr[high];
  arr[high] = temp;

  return i + 1;
}

function sort(arr, low, high) {
  if (low < high) {
    let part = partition(arr, low, high);

    sort(arr, low, part - 1);
    sort(arr, part + 1, high);
  }
}

function quickSort(arr) {
  sort(arr, 0, arr.length);
  arr.shift();
  return arr;
}
