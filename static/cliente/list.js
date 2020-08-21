// $(function () {
//     $('#data').DataTable({
//         responsive: true,
//         autoWidth: true,
//         destroy: true,
//         deferRender: true,
//         ajax: {
//             url: window.location.pathname,
//             type: 'POST',
//             data: {
//                 'action': 'searchdata'
//             },
//             dataSrc: ""
//         },
//         columns: [
//             {"data": "c.id"},
//             {"data": "c.nombre"},
//             {"data": "c.apellido"},
//             {"data": "c.dni"},
//             {"data": "c.email"},
//             {"data": "c.telefono"},
//             {"data": "c.direccion"},
//             {"data": "c.creado"},
//             {"data": "opciones"},
//         ],
//         columnDefs: [
//             {
//                 targets: [-1],
//                 class: 'text-center',
//                 orderable: true,
//                 render: function (data, type, row) {
//                     var buttons = '<a href="/SGCapp/clientes/edit/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
//                     buttons += '<a href="/SGCapp/clientes/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
//                     return buttons;
//                 }
//             },
//         ],
//         initComplete: function (settings, json) {
//             alert('Tabla cargada');
//         }
//     });
// });