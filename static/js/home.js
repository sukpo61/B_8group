$(document).ready(function () {
            show_comment()
        });


        function save_kimm() {

            let name = $('#name').val()
            let comment = $('#comment').val()
            let person = "kimm"

            $.ajax({
                type: 'POST',
                url: '/comment',
                data: {'name_give' : name, 'comment_give' : comment, 'person' : person},
                success: function (response) {
                    console.log(response)
                    window.location.reload()
                }
            })
        }

        function show_comment() {
            $.ajax({
                type: "GET",
                url: "/comment",
                data: {},
                success: function (response) {
                    let rows = response['comments']
                    for (i = 0; i < rows.length; i++) {

                        let name = rows[i]['name']
                        let comment = rows[i]['comment']
                        let person = rows[i]['person']

                        let temp_html = `<div class="card">
                                            <div class="card-body">
                                                <blockquote class="blockquote mb-0">
                                                    <p>${comment}</p>
                                                    <footer class="blockquote-footer">${name}</footer>
                                                </blockquote>
                                            </div>
                                        </div>`

                        if(person == "kimm"){
                            $("#comment-list").append(temp_html)
                        }else{
                            $("#comment-list").append()
                        }

                    }
                }
            });
        }