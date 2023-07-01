class File_Content:

    def ReturnContentByExtension(nombre_archivo, _extension):

        file_Content = ''

        if (_extension == 'js'):
            file_Content = '''
            $(document).ready( function () {
                getActualDate();
            });

            function getActualDate() {
                // Date object
                const date = new Date();

                let currentDay = String(date.getDate()).padStart(2, '0');

                let currentMonth = String(date.getMonth() + 1).padStart(2, "0");

                let currentYear = date.getFullYear();

                // we will display the date as DD/MM/YYYY 

                let currentDate = `${currentDay}/${currentMonth}/${currentYear}`;

                //console.log("The current date is " + currentDate);

                $("#txtFecha_OC").val(currentDate)
            }

            '''
        elif _extension == 'cs':
            _nameSpace = input(
                'Ingrese el espacio de nombres del controllador (Namespace): ')

            file_Content = (
                f'using Microsoft.AspNetCore.Mvc;\n'
                f'using {_nameSpace}.Models;\n'
                f'using System.Diagnostics;\n\n'
                f'namespace {_nameSpace}.Controllers\n'
                '{\n'
                f'    public class {nombre_archivo}Controller : Controller\n'
                '    {\n'
                f'        public IActionResult {nombre_archivo}()\n'
                '        {\n'
                # '            return View();\n'
                f'            return View(@"~\Views\{nombre_archivo}\{nombre_archivo}.cshtml");'
                '        }\n'
                '    }\n'
                '}\n'
            )
            nombre_archivo = f'{nombre_archivo}Controller'
        elif _extension == 'cshtml':

            _title_view = input(
                "Ingrese titulo de la vista (ViewBag.Title,h1): ")
            _nameJs = input("Ingrese el nombre del Js de la vista: ")

            file_Content = (
                '@{\n'
                f'    ViewBag.Title = "{_title_view}";\n\n'
                '    var sessionId = Context.Request.Cookies["SessionId"];\n'
                '    var userRole = Context.Request.Cookies["SessionRol"];\n'
                '    var userName = Context.Request.Cookies["SessionUName"];\n'
                '    var userSurName = Context.Request.Cookies["SessionUSur"];\n'
                '    var userlk = Context.Request.Cookies["Sessionlk"];\n\n'
                '    var _model = new SessionModel();\n\n'
                '    if (sessionId == null)\n'
                '    {\n'
                '        _model = new SessionModel();\n'
                '    }\n'
                '    else\n'
                '    {\n'
                '        _model = new SessionModel()\n'
                '        {\n'
                '            Apellido = userSurName,\n'
                '            lk = userlk,\n'
                '            Nombre = userName,\n'
                '            rol = userRole,\n'
                '        };\n'
                '    }\n'
                '}\n\n'
                '@if (sessionId == null)\n'
                '{\n'
                '    <script src="~/lib/jquery/dist/jquery.min.js"></script>\n\n'
                '    <script>\n\n'
                '        $(document).ready(function () {\n'
                '            var currentURL = $(location).attr(\'href\').split(\'/\');\n\n'
                '            let returnURL = currentURL[0] + "//" + currentURL[2] + "/";\n'
                '            window.location.replace(returnURL);\n'
                '        })\n'
                '    </script>\n'
                '}\n'
                'else\n'
                '{\n\n'
                '    <div class="Container-body">\n\n'
                f'        <h1>{_title_view}</h1>\n'
                '        <br />\n'
                '        <div class="card-body">\n'
                '        </div>\n'
                '    </div>\n'
                '}\n'
                '    @section scripts{'
                f'<script src="~/js/APP/{_nameJs}.js" crossorigin="anonymous"></script>'
                '}'
            )
        elif _extension == 'partial':
            _nameSpace = input(
                'Ingrese el espacio de nombres del controllador (Namespace): ')
            _nameModel = input(
                f'Ingrese el nombre del modelo ({_nameSpace}.Models.nombremodelo): ')
            _tableid = input(
                f'Ingrese el nombre del ID de tabla (ex. TableResultados): ')

            file_Content = (
                f'@using {_nameSpace}.Models;\n'
                '\n'
                f'@model {_nameSpace}.Models.{_nameModel}\n'
                '\n'
                '@{\n'
                '    var sessionId = Context.Request.Cookies["SessionId"];\n'
                '    var userRole = Context.Request.Cookies["SessionRol"];\n'
                '    var userName = Context.Request.Cookies["SessionUName"];\n'
                '    var userSurName = Context.Request.Cookies["SessionUSur"];\n'
                '    var userlk = Context.Request.Cookies["Sessionlk"];\n\n'
                '    var _model = new SessionModel();\n\n'
                '    if (sessionId == null)\n'
                '    {\n'
                '        _model = new SessionModel();\n'
                '    }\n'
                '    else\n'
                '    {\n'
                '        _model = new SessionModel()\n'
                '        {\n'
                '            Apellido = userSurName,\n'
                '            lk = userlk,\n'
                '            Nombre = userName,\n'
                '            rol = userRole,\n'
                '        };\n'
                '    }\n'
                '}\n\n'
                '<br />\n'
                f'<table class="table" id="{_tableid}">\n'
                '    <thead>\n'
                '        <tr>\n'
                '            <th></th>\n'
                '            <th>\n'
                '                ID\n'
                '            </th>\n'
                '        </tr>\n'
                '    </thead>\n'
                '    <tbody>\n'
                '        @foreach (var item in Model.listaElementos)\n'
                '        {\n'
                '            <tr>\n'
                '                <td class="glyphicon glyphicon-triangle-bottom"></td>\n'
                '                <td>\n'
                '                    @Html.DisplayFor(modelitem => item.modelId)\n'
                '                </td>\n'
                '            </tr>\n'
                '        }\n'
                '    </tbody>\n'
                '</table>\n'
            )

        return file_Content, nombre_archivo
