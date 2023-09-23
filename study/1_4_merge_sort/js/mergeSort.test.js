import { it, expect } from 'vitest'

import { mergeSort } from './mergeSort.js'

it('should sort an array', () => {
  expect(mergeSort([4, 2, 1, 3])).toEqual([1, 2, 3, 4])
})

it('should sort an array with duplicates', () => {
  expect(mergeSort([4, 2, 1, 3, 4])).toEqual([1, 2, 3, 4, 4])
})
