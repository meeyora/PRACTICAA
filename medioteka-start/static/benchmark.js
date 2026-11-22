const button = document.getElementById('run');
button.addEventListener('click', () => {
  const begin = performance.now();
  let checksum = 0;
  for (let i = 1; i <= 5000000; i += 1) {
    checksum = (checksum + (i % 97)) % 1000000007;
  }
  const elapsed = performance.now() - begin;
  document.getElementById('result').textContent =
    `Время: ${elapsed.toFixed(3)} мс\nКонтрольная сумма: ${checksum}`;
});
