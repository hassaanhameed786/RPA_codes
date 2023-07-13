var month_obj = {
    "Jan": "01",
    "Feb": "02",
    "Mar": "03",
    "Apr": "04",
    "May": "05",
    "Jun": "06",
    "Jul": "07",
    "Aug": "08",
    "Sep": "09",
    "Oct": "10",
    "Nov": "11",
    "Dec": "12"
};
var dt = ${Invoice_date};  // reference variable from above componenet of the flow
var mn_list = dt.split("-");
var mon_no = month_obj[mn_list[1]];
var dd = mn_list[0] + "/" + mon_no + "/" + mn_list[2];
return dd;
