$(document).ready(function () {
            show_home()
        });

        function show_home() {
            $.ajax({
                type: "GET",
                url: "/home",
                data: {},
                success: function (response) {
                    console.log('성공')
                    let rows = response['comments']
                    for (let i = 0; i < rows.length; i++) {
                        let name = rows[i]['name']
                        let comment = rows[i]['comment']
                        let num = rows[i]['num']
                        let done = rows[i]['done']

                        let temp_html = ``
                        if (done == 0) {
                            temp_html = `<li>
                                    <h2>${name}</h2>
                                    <h2>${comment}</h2>
                                    <button onclick="done_home(${num})" type="button" class="btn btn-outline-primary">댓글 지우기</button>
                                </li>`
                        }
                        $('#comment-list').append(temp_html)
                    }
                }
            });
        }

        function save_home() {
            let name = $('#name').val()
            let comment = $('#comment').val()

            $.ajax({
                type: "POST",
                url: "/home",
                data: {name_give: name, comment_give: comment},
                success: function (response) {
                    alert(response["msg"])
                    window.location.reload()
                }
            });
        }

        function done_home(num) {
            $.ajax({
                type: "POST",
                url: "/home/done",
                data: {num_give: num},
                success: function (response) {
                    alert(response["msg"])
                    window.location.reload()
                }
            });
        }
