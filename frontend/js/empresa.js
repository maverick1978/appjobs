$(document).ready(function() {
    $('#createVacancy').click(function() {
        $('#vacancyPopup').modal('show');
    });

    $('#vacancyForm').submit(function(event) {
        event.preventDefault();
        var formData = {
            profession: $('#profession').val(),
            description: $('#description').val(),
            salary: $('#salary').val(),
            availabilityDate: $('#availabilityDate').val()
        };

        $.post('/create_vacancy', formData, function(response) {
            alert('Vacante creada exitosamente');
            $('#vacancyPopup').modal('hide');
            // Lógica para agregar la nueva vacante al contenedor de vacantes
        });
    });

    $('#searchCandidates').click(function() {
        // Lógica para buscar candidatos
    });
});
