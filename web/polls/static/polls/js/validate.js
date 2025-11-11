document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (event) {
    const selected = document.querySelector("input[name='choice']:checked");
    let alertBox = document.querySelector(".alert-text");

    if (!selected) {
      event.preventDefault(); // 送信を中止する

      // すでにアラートが存在する場合はテキストを更新するだけ
      if (alertBox) {
        alertBox.textContent = "投票するには必ず一つ選択してください。フロント";
      } else {
        const div = document.createElement("div");
        div.className = "alert alert-danger d-flex align-items-center mt-2";
        div.innerHTML = `
          <svg class="bi flex-shrink-0 me-2" width="20" height="20" role="img" aria-label="Danger:">
            <use xlink:href="#exclamation-triangle-fill"></use>
          </svg>
          <span class="alert-text">投票するには必ず一つ選択してください。フロント</span>
        `;
        form.prepend(div);
      }
    }
  });
});
