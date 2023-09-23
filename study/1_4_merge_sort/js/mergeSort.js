export function mergeSort(arr) {
  // base case
  if (arr.length === 1) return arr

  // divide
  const midPoint = Math.floor(arr.length / 2)
  const left = arr.slice(undefined, midPoint)
  const right = arr.slice(midPoint)

  const leftSorted = mergeSort(left)
  const rightSorted = mergeSort(right)

  // merge
  return merge(leftSorted, rightSorted)
}

function merge(left, right) {
  let i = 0,
    j = 0

  let arr = []
  while (i < left.length && j < right.length) {
    // pick the smaller one
    if (left[i] < right[j]) {
      arr.push(left[i])
      i = i + 1
    } else {
      arr.push(right[j])
      j = j + 1
    }
  }
  const leftRemained = left.splice(i)
  const rightRemained = right.splice(j)

  return arr.concat(leftRemained).concat(rightRemained)
}
