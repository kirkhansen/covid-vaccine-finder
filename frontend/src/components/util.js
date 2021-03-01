export function* enumerate(array) {
  for (let i = 0; i < array.length; i += 1) {
    yield [i, array[i]];
  }
}
