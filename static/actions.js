let teach_log_form = document.querySelector('#teach-log');
let stu_log_form = document.querySelector('#stu-log');
let stu_reg_form = document.querySelector('#stu-reg');
let teach_reg_form = document.querySelector('#teach-reg');
let form_detail = document.querySelector('#form-detail');
let stu_img = document.querySelector('#stu-img');
let teach_img = document.querySelector('#teach-img');
let role_teach = document.querySelector('#role-ch2');
let role_stu = document.querySelector('#role-ch3');



function teach_log()
{
    teach_log_form.style.display = 'block';
    teach_reg_form.style.display = 'none';
    stu_reg_form.style.display = 'none';
    stu_log_form.style.display = 'none';
    form_detail.style.height = '60%';

    teach_img.style.border = '3px solid black';
    stu_img.style.border = '1px solid black';
    role_teach.style.color = 'black';
    role_stu.style.color = 'rgba(0, 0, 0, 0.5)';
}

function stu_log()
{
    teach_log_form.style.display = 'none';
    teach_reg_form.style.display = 'none';
    stu_reg_form.style.display = 'none';
    stu_log_form.style.display = 'block';
    form_detail.style.height = '60%';

    stu_img.style.border = '3px solid black';
    teach_img.style.border = '1px solid black';
    role_teach.style.color = 'rgba(0, 0, 0, 0.5)';
    role_stu.style.color = 'black';
}

function show_stu_reg()
{
    teach_log_form.style.display = 'none';
    teach_reg_form.style.display = 'none';
    stu_reg_form.style.display = 'block';
    stu_log_form.style.display = 'none';
    form_detail.style.height = '95%';
}

function show_teach_reg()
{
    teach_log_form.style.display = 'none';
    teach_reg_form.style.display = 'block';
    stu_reg_form.style.display = 'none';
    stu_log_form.style.display = 'none';
    form_detail.style.height = '80%';
}