/* @odoo-module */
 
import { GanttRenderer } from "@web_gantt/gantt_renderer";
 
import { useEffect, onWillStart } from "@odoo/owl";
 
export class StockTransportGanttRenderer extends GanttRenderer {
    setup() {
        super.setup();
        
        onWillStart(this.onWillStart);
    }

    async onWillStart() {
        
    }
}
 
StockTransportGanttRenderer.pillTemplate = "stock_transport.PlanningGanttRenderer.Pill";
StockTransportGanttRenderer.components = {
    ...GanttRenderer.components,
     
};
