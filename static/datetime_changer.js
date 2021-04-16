var datetimes = document.querySelectorAll(".idea-card i");
var DateTime = luxon.DateTime;
for (var sdt of datetimes) {
    dt = DateTime.fromSQL(sdt.innerText);
    sdt.innerText = dt.setLocale('ru').toFormat('d MMMM tt');

}