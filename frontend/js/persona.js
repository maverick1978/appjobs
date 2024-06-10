$(document).ready(function() {
    $('#searchVacancies').click(function() {
        $('#vacancySearchPopup').modal('show');
    });

    $('#createResume').click(function() {
        $('#resumePopup').modal('show');
    });

    $('#resumeForm').submit(function(event) {
        event.preventDefault();
        var formData = new FormData(this);

        $.ajax({
            url: '/upload_resume',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                alert('Hoja de vida cargada con éxito');
                $('#resumePopup').modal('hide');
            },
            error: function(response) {
                alert('Error al cargar la hoja de vida');
            }
        });
    });
});
